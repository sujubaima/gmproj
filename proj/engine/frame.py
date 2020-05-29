# -- coding: utf-8 --

import uuid
import importlib
import time
import queue
import threading
import inspect

from proj import options
from proj.runtime import context
from proj.engine import script


class Mutable(object):

    def __init__(self, **kwargs):
        self.id = uuid.uuid1()
        self.initialize()
        self.load(**kwargs)
        #if len(kwargs) != 0:
        #    self.finish()

    def load(self, **kwargs):
        for k, v in kwargs.items():
            self.handle(k, v)
        self.finish()
        
    def handle(self, k, v):
        setattr(self, k, v)

    def initialize(self):
        pass

    def finish(self):
        pass        

    def __getattr__(self, k):
        return None
  

class MessageBase(Mutable):
    """
    用于存放一个order或action完成的结果，状态的改变；前端模块通过不断读取消息队列，
    将其转换为可展示的内容打印到控制台上；

    生成的消息不会立即执行，而是要等待到下一个order被提交。你也可以在生成一个消息后，显式
    调用sync接口，把之前的消息全部处理，前提是需要指定消息的handler；

    消息支持注册回调函数，如某个消息带有回调函数，则当该消息被处理之后会执行它。一般
    用于需要玩家交互的场景；

    虽然做限制，但建议sync与callback均通过order完成；因为order本身就有串联流程的功用，
    而action最好只用来处理某个动作或行为，不要与前端的设计有过多耦合；
    """
    Null = "Null"

    Show = "show"
    Input = "input"
    Ensure = "ensure"
    Options = "options"
    Conversation = "conv"

    BackMenu = "backmenu"
    PopMenu = "popmenu"

    WorldPlayer = "world_player"
    WorldThumbnail = "world_thumbnail"
    WorldMap = "world_map"
    WorldClash = "world_clash"
    WorldProcess = "world_process"

    WorldMovePosition = "world_move_position"

    WorldTalkPosition = "world_talk_position"
    WorldTalkObject = "world_talk_object"
    
    WorldGivePosition = "world_give_position"
    WorldGiveObject = "world_give_object"
    WorldGiveItem = "world_give_item"

    WorldExplorePosition = "world_explore_position"
    WorldExploreTool = "world_explore_tool"

    WorldBuildPosition = "world_build_position"
    WorldBuildPlan = "world_build_plan"

    WorldAttackPosition = "world_attack_position"
    WorldAttackEnsure = "world_attack_ensure"
    
    WorldScenarioChangeEnsure = "world_scenario_change_ensure"
    
    WorldRest = "world_rest"

    BattleStart = "battle_start"
    BattlePlayer = "battle_player"
    BattleQuit = "battle_quit"
    BattleMap = "battle_map"
    BattleNewTurn = "battle_new_turn"
    BattleFinishTurn = "battle_finish_turn"
    BattleFinish = "battle_finish"
    BattleFinishSilent = "battle_finish_silent"

    BattleMovePosition = "battle_move_position"
    BattleMoveEnsure = "battle_move_ensure"
    BattleMoveStart = "battle_move_start"
    BattleMoveFinish = "battle_move_finish"

    BattleSkillChoose = "battle_skill_choose"
    BattleSkillPosition = "battle_skill_position"
    BattleSkillEnsure = "battle_skill_ensure"
    BattleSkillStart = "battle_skill_start"
    BattleSkillFinish = "battle_skill_finish"

    BattleItemChoose = "battle_item_choose"
    BattleItemPosition = "battle_item_position"
    BattleItemEnsure = "battle_item_ensure"
    BattleItemStart = "battle_item_start"
    BattleItemFinish = "battle_item_finish"
    
    BattlePersonChoose = "battle_person_choose"

    BattleRestStart = "battle_rest_start"
    BattleRestFinish = "battle_rest_finish"
    
    PersonSpeak = "person_speak"
    PersonDialogBranch = "person_dialog_branch"
    PersonStudySkill = "person_study_skill"
    
    PersonItemChoose = "person_item_choose"
    PersonItemQuantity = "person_item_quantity"
    PersonItemObject = "person_item_object"
    PersonItemTransfer = "person_item_transfer"
    PersonItemAcquire = "person_item_acquire"
    PersonItemLost = "person_item_lost"
    PersonItemEquip = "person_item_equip"
    
    PersonRecipe = "person_recipe"
    PersonRecipeChoose = "person_recipe_choose"
    PersonRecipeEnsure = "person_recipe_ensure"
    PersonRecipeLearn = "person_recipe_learn"
    
    PersonEquipment = "person_equipment"
    PersonEquipOn = "person_equip_on"
    PersonEquipInlayChoose = "person_equip_inlay_choose"
    PersonEquipRepair = "person_equip_repair"

    PersonSkill = "person_skill"
    PersonSkillChoose = "person_skill_choose"
    PersonSkillLearn = "person_skill_learn"
    
    PersonExpGain = "person_exp_gain"
    
    PersonTrade = "person_trade"
    
    PersonTaskUpdate = "person_task_update"
    PersonAttitudeChange = "person_attitude_change"
    
    PersonJoinTeam = "person_join_team"
    
    TeamTransport = "team_transport"
    
    SuperSkillChoose = "superskill_choose"
    SuperSkillRead = "superskill_read"

    GameFail = "game_fail"

    Status = "status"
    Effect = "effect"
    
    ActionFinish = "action_finish"
    
    handler = None
    
    def initialize(self):
        self.callback = None


class MessageMultipleThread(MessageBase):

    All = queue.Queue()
    
    empty = threading.Event()
    nempty = threading.Event()

                
    @staticmethod
    def sync():
        wait_order = False
        for i in inspect.stack():
            if i.function == "handler":
                wait_order = True
                break
        if wait_order:
            Order.empty.wait()
        else:
            Message.empty.wait()
        
    def finish(self):
        Message.All.put(self)
        Message.empty.clear()
        Message.nempty.set()
        
        
class MessageSingleThread(MessageBase):

    All = []

    @staticmethod
    def sync():
        if Message.handler is not None:
            while len(Message.All) > 0:
                msg = Message.All.pop(0)
                Message.handler(msg)
                
    def finish(self):
        Message.All.append(self)


class Action(Mutable):
    """
    用于描述游戏中的一个行为，与是否玩家操作无关；
    例如：
    XXX获取XXX个物品
    XXX从A点移动至B点
    XXX对XXX施放了XXX技能
    除去流程控制相关的逻辑外，Order与Event产生的效果都应该是通过调用对应的Action来完成；
    """

    #All = []

    #@staticmethod
    #def empty():
    #    return len(Action.All) == 0

    #@staticmethod
    #def handle():
    #    while not Action.empty():
    #        ac = Action.All.pop(0)
    #        ac.do()

    #def finish(self):
    #    Action.All.append(self)

    def do(self):
        pass


class OrderBase(Mutable):

    events = {}

    Current = None

    @staticmethod
    def addevent(evt):
        if evt.ordername not in OrderBase.events:
            OrderBase.events[evt.ordername] = [[], []]
        OrderBase.events[evt.ordername][evt.phase].append(evt)

    def initialize(self):
        self.canceled = False

    def solve(self):
        OrderBase.Current = self
        ordername = self.__class__.__name__
        if ordername in OrderBase.events:
            triggered = set()
            while Event.pick(OrderBase.events[ordername][0], triggered) is not None:
                Message.sync()
        if not self.canceled:
            self.carry()
        if ordername in OrderBase.events:
            triggered = set()
            while Event.pick(OrderBase.events[ordername][1], triggered) is not None:
                Message.sync()
        OrderBase.Current = None

    def carry(self):
        pass
        


class OrderMultipleThread(OrderBase):

    hub = False

    All = []
    
    empty = threading.Event()
    nempty = threading.Event()
    
    @staticmethod
    def sync():
        wait_msg = False
        for i in inspect.stack():
            if i.function == "carry":
                wait_msg = True
                break
        if wait_msg:
            Message.empty.wait()
        else:
            Order.empty.wait()
            
    def finish(self):       
        if self.__class__.__name__ != "WorldProcessOrder":
            pos = len(Order.All)
            for idx, itm in enumerate(reversed(Order.All)):
                if not itm.hub:
                    pos = idx
                    break
        else:
            pos = 0
        Order.All.insert(len(Order.All) - pos, self) 
        Order.empty.clear()
        Order.nempty.set()        
        
        #if self.__class__.__name__ == "WorldProcessOrder":
        #    Message.empty.wait()
        #if not self.eventless:
        #    while Event.pick() is not None:
        #        Message.empty.wait()
        #self.carry()


class OrderSingleThread(OrderBase):
    """
    阀门模块，在每个order执行前，前端都把所有尚未处理的消息消化掉，
    同时对可触发事件进行一轮检查；

    主要应用于以下场景：
    1、用户主动下达的指令，可以视为一个order；
    2、对某些复杂的系统进行流程控制，如战斗、大地图等；
    2、某些中间需要等待消息同步的复杂操作，建议插入一个order，而不是直接在action中编写回调；
    """

    hub = False

    Previous = None
    Next = None
    
    @staticmethod
    def sync():
        Message.sync()
        while Order.Next is not None:
            o = Order.Next
            Order.Previous = o
            Order.Next = None
            o.solve()
            Message.sync()

    def finish(self):
        if self.hub:
            Order.sync()
        Order.Next = self


if options.MULTIPLE_THREAD:
    Message = MessageMultipleThread
    Order = OrderMultipleThread
    Message.empty.set()
    Order.empty.set()
else:
    Message = MessageSingleThread
    Order = OrderSingleThread


class Event(Mutable):
    """
    事件模块，在每一个order执行前会进行检查，满足条件的事件会连锁触发；
    事件链条构成游戏的整个流程；
    """

    All = {}
    
    def _handle(self, k, v):
        actions = importlib.import_module("proj.builtin.actions")
        conditions = importlib.import_module("proj.builtin.conditions")
        if k == "scripts":
            for vtpl in v:
                tp = vtpl["type"]
                self.actions.append(eval("actions.%s" % tp)(**script.entitify(vtpl)))
        elif k == "conditions":
            for vtpl in v:
                tp = vtpl["type"]
                self.conditions.append(eval("conditions.%s" % tp)(**script.entitify(vtpl)))
        else:
            setattr(self, k, v)

    def initialize(self):
        self.id = None
        self.name = None

        self.active = False
        self.triggered = False
        self.retrigger = False
        self.ordername = "WorldProcessOrder"
        self.phase = 1
        
        self.scripts = []
        self.conditions = []

    def finish(self):
        Event.add(self)

    @staticmethod
    def add(e):
        Event.All[e.id] = e
        if e.active:
            Order.addevent(e)

    @staticmethod
    def get(id):
        return Event.All.get(id, None)

    @staticmethod
    def pick(eventlist, triggered):
        deleted = []
        chosen = None
        for i, e in enumerate(eventlist):
            if not e.active:
                deleted.append(e)
                continue
            if e.id in triggered and not e.retrigger:
                continue
            if not e.condition():
                continue
            deleted.append(e)
            chosen = e
            break
        for e in deleted:
            eventlist.remove(e)
        if chosen is not None:
            chosen.triggered = True;
            chosen.active = False
            triggered.add(e.id)
            chosen.run()
        return chosen

    def turn(self, onoff):
        new_sts = (onoff == "on")
        if self.active == new_sts:
            return
        self.active = new_sts
        if self.active:
            self.active_time = context.timestamp_
            Order.addevent(self)

    def condition(self):
        if len(self.conditions) == 0:
            return True
        return script.conditions(self.conditions)

    def run(self):
        script.run(self.scripts)
        
        
class Condition(Mutable):

    def initialize(self):
        self.expect = True

    def check(self):
        return True
        
        

                                                
