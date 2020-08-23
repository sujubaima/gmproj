# -- coding: utf-8 --

import uuid
import importlib
import time
import queue
import threading
import inspect
import traceback

from concurrent.futures import ThreadPoolExecutor

from proj import options


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
  

class Message(Mutable):
    
    Null = "Null"

    Show = "show"
    Input = "input"
    Ensure = "ensure"
    Options = "options"
    Conversation = "conv"
    Halt = "halt"

    BackMenu = "backmenu"
    PopMenu = "popmenu"

    ShowMacros = "show_macros"
    
    ControlTest = "control_test"

    EnsureControl = "ensure_control"
    BranchControl = "branch_control"

    PersonSelectControl = "person_select_control"
    PersonSelectMultipleControl = "person_select_multiple_control"
    PersonStatusControl = "person_status_control"
    PositionSelectControl = "pos_select_control"
    ItemSelectControl = "item_select_control"
    ItemInlaySelectControl = "item_inlay_select_control"
    ItemUsageControl = "item_usage_control"
    ItemQuantitySelectControl = "item_quantity_select_control"
    RecipeSelectControl = "recipe_select_control"

    SkillControl = "skill_control"
    SkillSelectControl = "skill_select_control"
    SkillNodeSelectControl = "skill_node_select_control"
    SuperskillSelectControl = "superskill_select_control"
    SuperskillControl = "superskill_control"

    EquipmentControl = "equip_control"

    ScenarioControl = "scenario_control"
    ScenarioChangeControl = "scenario_change_control"
    ThumbnailControl = "thumbnail_control"
    
    ExploreToolSelectControl = "explore_tool_select_control"

    RestControl = "rest_control"

    TeamControl = "team_control"

    TransportControl = "transport_control"

    TradeControl = "trade_control"

    BattleControl = "battle_control"
    BattleMapControl = "battle_map_control"
    BattlePositionSelectControl = "battle_pos_select_control"
    BattleScopeControl = "battle_scope_control"

    SystemControl = "system_control"
    EventSelectControl = "event_select_control"
    EventDetailControl = "event_detail_control"
    FileSelectControl = "file_select_control"

    BattleStart = "battle_start"
    BattlePlayer = "battle_player"
    BattleQuit = "battle_quit"
    BattleMap = "battle_map"
    BattleNewTurn = "battle_new_turn"
    BattleFinishTurn = "battle_finish_turn"
    BattleFinish = "battle_finish"
    BattleFinishSilent = "battle_finish_silent"
    BattleSequence = "battle_sequence"

    BattleMove = "battle_move"
    BattleSkillScope = "battle_skill_scope"
    BattleSkill = "battle_skill"
    BattleItemScope = "battle_item_scope"
    BattleItem = "battle_item"
    BattleRest = "battle_rest"
    
    PersonSpeak = "person_speak"
    PersonStudySkill = "person_study_skill"
    
    PersonItemTransfer = "person_item_transfer"
    PersonItemAcquire = "person_item_acquire"
    PersonItemLost = "person_item_lost"
    PersonItemEquip = "person_item_equip"
    
    PersonRecipe = "person_recipe"
    PersonRecipeLearn = "person_recipe_learn"
    
    PersonEquipment = "person_equipment"
    PersonEquipOn = "person_equip_on"
    PersonEquipRepair = "person_equip_repair"

    PersonSkill = "person_skill"
    PersonSkillLearn = "person_skill_learn"
    
    PersonExpGain = "person_exp_gain"
    
    PersonTaskUpdate = "person_task_update"
    PersonAttitudeChange = "person_attitude_change"
    
    PersonJoinTeam = "person_join_team"
    
    TeamTransport = "team_transport"

    WorldMap = "world_map"
    
    SuperskillRead = "superskill_read"

    GameFail = "game_fail"

    Status = "status"
    Effect = "effect"
    
    ActionFinish = "action_finish"
    
    handler = None

    All = queue.Queue()

    empty = threading.Event()
    
    def initialize(self):
        self.callback = None
                
    @staticmethod
    def sync():
        Message.empty.wait()
        
    def finish(self):
        Message.All.put(self)
        Message.empty.clear()
        
        
class Action(Mutable):

    events = {}

    @staticmethod
    def addevent(evt):
        if evt.action not in Action.events:
            Action.events[evt.action] = [[], []]
        Action.events[evt.action][evt.phase].append(evt) 

    def initialize(self):
        self.canceled = False

    def do(self):
        name = self.__class__.__name__
        if name in Action.events:
            triggered = set()
            while Event.pick(Action.events[name][0], triggered) is not None:
                Message.sync()
        if self.canceled:
            return
        self.take()
        name = self.__class__.__name__
        if name in Action.events:
            triggered = set()
            while Event.pick(Action.events[name][1], triggered) is not None:
                Message.sync()

    def take(self):
        pass


class Control(Mutable):

    All = []

    thpool = ThreadPoolExecutor(max_workers=8)

    @staticmethod
    def showmsg(worker):
        worker_exception = worker.exception()
        if worker_exception:
            print(traceback.format_exc(worker_exception))

    @staticmethod
    def listener(func):
        """
        监听方法每次通过线程调起，避免阻塞主线程
        """
        def _listener(*args, **kwargs):
            #th = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
            #th.start()
            task = Control.thpool.submit(func, *args, **kwargs)
            task.add_done_callback(Control.showmsg)
        return _listener

    def initialize(self):
        self.cond = threading.Condition() 

    def finish(self):
        self.macs, self.macs_desc = self.macros()
        self.macs["#macros"] = self.showmacros
        self.macs_desc["#macros"] = "显示所有的宏指令"

    def macros(self):
        return {}, {}

    def showmacros(self, macro):
        Message(style=Message.ShowMacros, control=self)

    def launch(self):
        """
        控件初始化方法，向绘图线程队列发送信息
        各控件自行实现初始化逻辑
        """
        pass

    def close(self):
        """
        关闭控件
        """
        self.cond.acquire()
        self.cond.notifyAll()
        self.cond.release()
        #Control.All.remove(self)
        Control.All.pop()

    def run(self):
        Control.All.append(self)
        self.cond.acquire()
        self.launch()
        self.cond.wait()
        self.cond.release()

    #def run(self):
    #    self.th = threading.Thread(target=self._run, daemon=True)
    #    self.th.start()


class Event(Mutable):
    """
    事件模块，在每一个order执行前会进行检查，满足条件的事件会连锁触发；
    事件链条构成游戏的整个流程；
    """

    All = {}

    def initialize(self):
        self.id = None
        self.name = None

        self.active = False
        self.triggered = False
        self.retrigger = False
        self.action = "WorldProcessAction"
        self.phase = 1
        self.active_time = 0
        
        self.scripts = []
        self.conditions = []

    def finish(self):
        Event.add(self)

    @staticmethod
    def add(e):
        Event.All[e.id] = e
        if e.active:
            Action.addevent(e)

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

    def turn(self, onoff, timestamp):
        new_sts = (onoff == "on")
        if self.active == new_sts:
            return
        self.active = new_sts
        if self.active:
            self.active_time = timestamp
            Action.addevent(self)

    def condition(self):
        if len(self.conditions) == 0:
            return True
        script = importlib.import_module("proj.engine.script")
        return script.conditions(self.conditions)

    def run(self):
        script = importlib.import_module("proj.engine.script")
        script.run(self.scripts)
        
        
class Condition(Mutable):

    def initialize(self):
        self.expect = True

    def check(self):
        return True  
