# -- coding: utf-8 --

from proj.engine import Action
from proj.engine import Message as MSG

from proj.entity import common
from proj.entity import Battle
from proj.entity import BattlePhase
from proj.entity import BattleEvent
from proj.entity import SkillType
from proj.entity import Person

from proj.runtime import context


class BattleAction(Action):

    def initialize(self):
        super(BattleAction, self).initialize()
        self.person_hooked = []
        
    def finish(self):
        if self.battle is None and self.subject is not None:
            self.battle = self.subject.team.battle

    def postdo(self):
        #for ac in self.additions:
        #    #MSG.sync()
        #    ac.do()
        while len(self.battle.additions) > 0:
            ac = self.battle.additions.pop(0)
            ac.do()
        for p in self.person_hooked:
            if self.battle.controllable():
                pass
            else:
                hooked_list = battle.ai.do(p)
                for h_ac in hooked_list:
                    MSG.sync()
                    h_ac.do()


class BattleStartAction(BattleAction):
    
    def take(self):
        self.battle = Battle(self.map, player=context.PLAYER, groups=self.groups, allies=self.allies, death=self.death, silent=self.silent)
        self.battle.start()
        context.battles[self.battle.id] = self.battle
        self.battle.reset_delta()
        self.battle.status_work(BattlePhase.Start)
        self.battle.deal()
        alivelist = []
        for alive in self.battle.alive:
            if alive.hp == 0:
                alivelist.append(alive)
        for alive in alivelist:
            BattleQuitAction(subject=alive, battle=self.battle).do()
        tmp_teams = set()
        for g in self.groups:
            for p in g:
                if p.team.id in tmp_teams:
                    continue
                p.team.process = context.timestamp + 1
                tmp_teams.add(p.team.id)
        self.snapshot = self.battle.snapshot(False)
        if not self.battle.silent:
            MSG(style=MSG.BattleStart, action=self)
            context.timeflow(1)
        return self.battle


class BattleJoinAction(BattleAction):

    def take(self):
        self.battle.append_group(group=self.group, allies=self.ally)
        self.battle.death = self.death
        tmp_teams = set()
        for p in self.group:
            if p.team.id in tmp_teams:
                continue
            p.team.process = context.timestamp + 1
            tmp_teams.add(p.team.id)
        self.battle.silent = False
        self.snapshot = self.battle.snapshot(False)
        MSG(style=MSG.BattleStart, action=self)
        context.timeflow(1)
        return self.battle


class BattleFinishAction(BattleAction):

    def do_unsilent(self):
        result = context.PLAYER.team.result
        explist = []
        nodelist = []
        itemlist = []
        if result:
            for p in self.battle.all:
                if p.team != context.PLAYER.team:
                    continue
                exp = self.battle.exps[p.id]
                explist.append((p, exp))
                if p.studying is not None:
                    p.exp += exp
                    if p.exp >= p.studying.exp:
                        nodelist.append((p, p.studying))
                        p.studying.learn(p)
                        p.studying = None
                        p.exp = 0
        self.result = result
        self.explist = explist
        self.nodelist = nodelist
        self.itemlist = itemlist 
        MSG(style=MSG.BattleFinish, action=self)

    def do_silent(self):
        MSG(style=MSG.BattleFinishSilent, action=self)

    def do_remove(self):
        teamwinner = None
        teamloser = None
        teamset = set()
        for p in self.battle.all:
            if p.team.id in teamset:
                continue
            teamset.add(p.team.id)
            if not p.team.result:
                if teamloser is None:
                    teamloser = p.team
                p.team.scenario.remove(p.team)
                p.team.scenario = None
                context.teams.pop(p.team.id)
            else:
                if teamwinner is None:
                    teamwinner = p.team
            #p.team.follow = None
            #p.team.target = p.team.stash.get("target", None)
        self.teamwinner = teamwinner
        self.teamloser = teamloser

    def take(self):
        self.battle.reset_delta()
        self.battle.status_work(BattlePhase.Finish)
        self.battle.deal()
        self.battle.finish()
        if self.battle.map.tpl_id.find("WORLD") >= 0:
            self.do_remove()
        context.battles.pop(self.battle.id)
        if not self.battle.silent:
            self.do_unsilent()
        else:
            self.do_silent()


class BattleNewTurnAction(BattleAction):

    def take(self):
        BattleFinishTurnAction(battle=self.battle).do()
        self.battle.sequence.append({"current": self.battle.current, "action": Action(), "results": {}})
        alivelist = []
        for alive in self.battle.alive:
            if alive.hp == 0:
                alivelist.append(alive)
        for alive in alivelist:
            BattleQuitAction(subject=alive, battle=self.battle).do()
        if self.battle.finished():
            return
        self.battle.start_turn()
        self.battle.sequence.append({"current": self.battle.current, "action": Action(), "results": {}})
        self.battle.reset_delta()
        self.battle.status_work(BattlePhase.StartTurn)
        self.battle.deal()
        self.snapshot = self.battle.snapshot(False)
        if not self.battle.silent:
            MSG(style=MSG.BattleNewTurn, action=self)
        alivelist = []
        for alive in self.battle.alive:
            if alive.hp == 0:
                alivelist.append(alive)
        for alive in alivelist:
            BattleQuitAction(subject=alive, battle=self.battle).do()


class BattleFinishTurnAction(BattleAction):

    def take(self):
        self.battle.finish_turn()
        self.battle.reset_delta()
        self.battle.status_work(BattlePhase.FinishTurn)
        self.battle.deal()
        self.snapshot = self.battle.snapshot(False)
        if len(self.battle.sequence) > 0 and \
           len(self.battle.sequence[-1]["results"]) > 0 and \
           not self.battle.silent:
            MSG(style=MSG.BattleFinishTurn, action=self)


class BattleQuitAction(BattleAction):

    def take(self):
        self.battle.status_work(BattlePhase.BeforeQuit)
        self.battle.quit(self.subject)
        if not self.battle.silent:
            MSG(style=MSG.BattleQuit, action=self)


class BattleMoveAction(BattleAction):

    def initialize(self):
        super(BattleMoveAction, self).initialize()
        self.motivated = True
        self.active = True
        self.redirect = True
        self.showmsg = True
        
    def do_move(self, active=True, redirect=True):
        """
        在战场的移动行为
        除了主动移动之外，被动移动（如某些效果触发）也会调用此接口
        参数active用于指定是否主动移动
        参数redirect用于指定该次移动主体是否发生朝向变化
        """
        oloc = self.battle.map.location(self.subject)
        if oloc == self.target and len(self.path) <= 1:
             return
        if active:
            self.battle.sequence.append({"current": self.battle.current, "action": self, "results": {}})
        self.battle.status_work(BattlePhase.BeforeMove)
        if oloc != self.target:
            self.battle.map.locate(self.subject, self.target)
        if redirect and len(self.path) > 1:
            self.subject.direction = self.battle.map.direction(self.path[1], self.path[0])
        self.battle.add_event(self.subject, BattleEvent.PositionMoved, trace=self.path)
        if len(self.battle.alive) == len(self.battle.map.entity_loc):
            self.battle.status_work(BattlePhase.AfterMove)

    def take(self):
        if self.subject.hp <= 0 or self.battle.finished():
            return
        if self.battle.current == self.subject and self.battle.moved[self.subject.id]:
            return
        self.battle.moved[self.subject.id] = True
        #self.battle.move(self)
        if self.active:
            self.battle.reset_delta()
        self.do_move(active=self.active, redirect=self.redirect)
        if self.active:
            self.battle.deal()
        self.snapshot = self.battle.snapshot()
        if not self.battle.silent and self.showmsg:
            MSG(style=MSG.BattleMove, action=self)
        alivelist = []
        for alive in self.battle.alive:
            if alive.hp == 0:
                alivelist.append(alive)
        for alive in alivelist:
            BattleQuitAction(subject=alive, battle=self.battle).do()
        self.postdo()


class BattleSkillAction(BattleAction):

    def initialize(self):
        super(BattleSkillAction, self).initialize()
        self.critical = False
        self.anti_list = []
        
    def do_attack(self):
        """
        战场的攻击行为
        """        
        self.battle.sequence.append({"current": self.battle.current, "action": self, "results": {}})
        self.battle.check_weapon_before(self.subject, self.skill)
        self.subject.mp_delta += -1 * self.skill.mp
        self.subject.correct()
        #self.battle.add_event(self.subject, BattleEvent.MPChanged, value=self.subject.mp_delta)
        self.critical = False
        self.battle.start_cd(self.subject, self.skill)
        self.skill.work(self.subject, battle=self.battle, phase=BattlePhase.BeforeAttack)
        self.battle.status_work(BattlePhase.BeforeAttack)
        should_hit = common.if_rate(self.subject.hit_rate)
        if not should_hit:
            self.battle.add_event(self.subject, BattleEvent.ACTFault)
        for q in self.objects:
            if self.battle.is_friend(self.subject, q):
                continue
            elif self.subject.hit_rate > 1:
                should_dodge = common.if_rate(1 - (1 - q.dodge_rate) * self.subject.hit_rate)
            else:
                should_dodge = common.if_rate(q.dodge_rate)
            # 失误与闪避在结果上不做区分，必要时可以通过是否有ACTFault来判断
            if not should_hit or should_dodge:
                self.battle.add_event(q, BattleEvent.ACTMissed)
        # 发动伤害计算前效果，实现得不是很优雅，后面考虑改一下
        self.skill.work(self.subject, battle=self.battle, phase=BattlePhase.BeforeDamage)
        self.battle.status_work(BattlePhase.BeforeDamage)
        for q in self.objects:
            if self.battle.event(q, BattleEvent.ACTMissed) is not None:
                continue
            hp_damaged, mp_damaged, critical, anti_damage = self.battle.damage(self.skill, self.subject, q)
            if anti_damage:
                self.battle.add_event(q, BattleEvent.ACTDefended)
                self.anti_list.append(q)
            if critical:
                self.battle.add_event(q, BattleEvent.ACTCritical)
            self.critical = self.critical or critical
            q.hp_delta = -1 * hp_damaged
            q.mp_delta = -1 * mp_damaged
        # 发动伤害计算后效果
        self.skill.work(self.subject, battle=self.battle, phase=BattlePhase.AfterDamage)
        self.battle.status_work(BattlePhase.AfterDamage)
        for q in self.battle.alive:
            q.correct()
            self.battle.add_event(q, BattleEvent.HPDamaged, value=q.hp_delta)
            self.battle.add_event(q, BattleEvent.MPDamaged, value=q.mp_delta)
        for q in self.objects:
            if self.battle.event(self.subject, BattleEvent.ACTFault) is not None:
                break
            should_counter = common.if_rate(q.counter_rate)
            if self.type != SkillType.Counter and should_counter and q.skill_counter is not None:
                self.battle.add_event(q, BattleEvent.Counter)
        self.battle.redirect(self.subject, self.objects, self.target, self.skill)
        # 发动后置效果
        self.skill.work(self.subject, battle=self.battle, phase=BattlePhase.AfterAttack)
        self.battle.status_work(BattlePhase.AfterAttack)
        for q in self.battle.alive:
            q.correct(poison=False)
            q.hp += q.hp_delta
            q.mp += q.mp_delta
            self.battle.add_event(q, BattleEvent.HPChanged, value=q.hp_delta)
            self.battle.add_event(q, BattleEvent.MPChanged, value=q.mp_delta)
        self.battle.check_weapon_after(self.subject, self.skill)
        ## 发动结算后效果
        #if should_hit:
        #    for ef in self.skill.effects:
        #        if ef.phase == BattlePhase.AfterSettlement:
        #            ef.work(self.subject, battle=self.battle)
        #self.battle.status_work(BattlePhase.AfterSettlement)
        for q in reversed(self.objects):
            p_tgt = self.battle.map.location(self.subject)
            #print(q.name)
            q_tgt = self.battle.map.location(q)
            if q.hp > 0 and self.subject.hp > 0 and \
               self.battle.event(q, BattleEvent.Counter) is not None:
                if not self.battle.skill_ava(q, q.skill_counter):
                    continue
                counter_range = self.battle.map.shape_scope(p_tgt, q.skill_counter.shape)
                if q_tgt not in counter_range:
                    continue
                counter_ac = BattleSkillAction(subject=q, battle=self.battle, 
                                               skill=q.skill_counter, target=p_tgt, scope=[p_tgt], 
                                               objects=[self.subject], type=SkillType.Counter)
                self.battle.additions.insert(0, counter_ac)
                #self.battle.attacked[q.id] = False

    def take(self):
        if self.subject.hp <= 0 or self.battle.finished():
            return
        if self.battle.current == self.subject and self.battle.attacked[self.subject.id]:
            return
            
        self.battle.moved[self.subject.id] = True
        self.battle.attacked[self.subject.id] = True
        self.battle.itemed[self.subject.id] = True
        self.battle.rested[self.subject.id] = True
        self.battle.reset = False

        map = self.battle.map
        p = self.battle.current

        # 计算技能作用范围
        if self.scope is None:
            self.scope = map.shape(map.location(p), self.target, self.skill.shape)

        # 计算技能作用范围内目标
        if self.objects is None:
            self.objects = []
            for ax, ay in self.scope:
                cp = map.loc_entity.get((ax, ay), None)
                if cp is not None and self.battle.skill_accept(self.skill, p, cp):
                    self.objects.append(cp)
                    
        self.objects = [obj for obj in self.objects if obj in self.battle.alive]
        if self.targets != "Grids" and len(self.objects) == 0:
            return

        self.snapshot = self.battle.snapshot(False)
        if not self.battle.silent:
            MSG(style=MSG.BattleSkillScope, action=self)
            MSG.sync()

        # 执行技能效果
        self.battle.reset_delta()
        self.do_attack()
        #self.battle.deal()
        self.snapshot = self.battle.snapshot()
        if not self.battle.silent:
            MSG(style=MSG.BattleSkill, action=self)
            # 这里因为当前的map实现不便将某一时刻全体对象的状态保存，因此必须保证MSG同步后再进行人员清算
            MSG.sync()

        # 清算败退
        alivelist = []
        for alive in self.battle.alive:
            if alive.hp == 0:
                alivelist.append(alive)
        for alive in alivelist:
            BattleQuitAction(subject=alive, battle=self.battle).do()

        #self.postdo()

        # 发动结算后效果
        if self.battle.event(self.subject, BattleEvent.ACTFault) is None:
            self.skill.work(self.subject, battle=self.battle, phase=BattlePhase.AfterSettlement)
        self.battle.status_work(BattlePhase.AfterSettlement)

        self.postdo()


class BattleItemAction(BattleAction):

    def do_item(self):
        """
        战场上的使用物品行为
        """       
        self.battle.sequence.append({"current": self.battle.current, "action": self, "results": {}})
        self.battle.status_work(BattlePhase.BeforeItem)
        should_hit = common.if_rate(self.subject.hit_rate)
        if not should_hit:
            self.battle.add_event(self.subject, BattleEvent.ACTFault)
        for q in self.objects:
            if self.battle.is_friend(self.subject, q):
                continue
            if self.subject.hit_rate > 1:
                should_dodge = common.if_rate(1 - (1 - q.dodge_rate) * self.subject.hit_rate)
            else:
                should_dodge = common.if_rate(q.dodge_rate)
            # 失误与闪避在结果上不做区分，必要时可以通过是否有ACTFault来判断
            if not should_hit or should_dodge:
                self.battle.add_event(q, BattleEvent.ACTMissed)
        self.item.work(self.subject, battle=self.battle)
        self.battle.redirect(self.subject, self.objects, self.target, self.item)
        for q in self.battle.alive:
            q.correct()
            q.hp += q.hp_delta
            q.mp += q.mp_delta
            self.battle.add_event(q, BattleEvent.HPChanged, value=q.hp_delta)
            self.battle.add_event(q, BattleEvent.MPChanged, value=q.mp_delta)
        self.battle.status_work(BattlePhase.AfterItem)

    def take(self):
        if self.subject.hp <= 0 or self.battle.finished():
            return
        if self.battle.current == self.subject and self.battle.itemed[self.subject.id]:
            return
            
        self.battle.moved[self.subject.id] = True
        self.battle.attacked[self.subject.id] = True
        self.battle.itemed[self.subject.id] = True
        self.battle.rested[self.subject.id] = True
        self.battle.reset = False

        map = self.battle.map
        p = self.battle.current

        # 计算技能作用范围
        if self.scope is None:
            self.scope = map.shape(map.location(p), self.target, self.item.shape)

        # 计算技能作用范围内目标
        if self.objects is None:
            self.objects = []
            for ax, ay in self.scope:
                cp = map.loc_entity.get((ax, ay), None)
                if cp is not None and self.battle.skill_accept(self.item, p, cp):
                    self.objects.append(cp)
                    
        self.objects = [obj for obj in self.objects if obj in self.battle.alive]
        if self.targets != "Grids" and len(self.objects) == 0:
            return

        if not self.battle.silent:
            MSG(style=MSG.BattleItemStart, action=self)
        # 执行技能效果
        self.battle.reset_delta()
        self.do_item()
        #self.battle.deal()
        if not self.battle.silent:
            MSG(style=MSG.BattleItem, action=self)
            # 这里因为当前的map实现不便将某一时刻全体对象的状态保存，因此必须保证MSG同步后再进行人员清算
            #MSG.sync()

        # 清算败退
        alivelist = []
        for alive in self.battle.alive:
            if alive.hp == 0:
                alivelist.append(alive)
        for alive in alivelist:
            BattleQuitAction(subject=alive, battle=self.battle).do()

        self.postdo()


class BattleRestAction(BattleAction):

    def do_rest(self):
        """
        战场的休息行为
        """        
        self.battle.sequence.append({"current": self.battle.current, "action": self, "results": {}})
        self.battle.status_work(BattlePhase.BeforeRest)
        p = self.subject
        if self.rest_action == 1:
            p.hp_delta = int(p.hp_limit * p.hp_recover_rate * p.hp_recover_rate_inferior)
            p.mp_delta = int(p.mp_limit * p.mp_recover_rate * p.mp_recover_rate_inferior)
        elif self.rest_action == 2:
            p.hp_delta = int(p.hp_limit * p.hp_recover_rate)
            p.mp_delta = int(p.mp_limit * p.mp_recover_rate)
        p.hp_delta = max(0, p.hp_delta - p.poison_hp)
        p.mp_delta = max(0, p.mp_delta - p.poison_mp)
        if p.hp_delta != 0 and p.mp_delta != 0:
            self.showmap = True
        else:
            self.showmap = False
        p.correct()
        p.hp += p.hp_delta
        p.mp += p.mp_delta
        self.battle.add_event(p, BattleEvent.HPChanged, value=p.hp_delta)
        self.battle.add_event(p, BattleEvent.MPChanged, value=p.mp_delta)
        self.battle.status_work(BattlePhase.AfterRest)

    def take(self):
        if self.subject.hp <= 0 or self.battle.finished():
            return
        if self.battle.attacked[self.subject.id] or self.battle.itemed[self.subject.id]:
            self.rest_action = 0
        elif self.battle.moved[self.subject.id]:
            self.rest_action = 1
        else:
            self.rest_action = 2
        self.battle.moved[self.subject.id] = True
        self.battle.attacked[self.subject.id] = True
        self.battle.itemed[self.subject.id] = True
        self.battle.rested[self.subject.id] = True
        self.battle.reset = False
        self.battle.reset_delta()
        self.do_rest()
        self.snapshot = self.battle.snapshot()
        #self.battle.deal()
        if not self.battle.silent and self.showmap:
            MSG(style=MSG.BattleRest, action=self)
        self.postdo()


class BattleOrderStatusAction(BattleAction):

    def take(self):
        if self.order == "move":
            status_map = self.battle.moved
        elif self.order == "attack":
            status_map = self.battle.attacked
        elif self.order == "item":
            status_map = self.battle.itemed
        elif self.order == "rest":
            status_map = self.battle.rested
        status_map[self.subject.id] = self.status
