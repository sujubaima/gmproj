# -- coding: utf-8 --

AttrText = \
  {"attack_": "基础攻击",
   "attack_factor_": "基础攻击",
   "defense_": "基础防御",
   "defense_factor_": "基础防御",
   "hit_rate_": "基础命中",
   "hit_rate_factor_": "命中率",
   "counter_rate_": "基础反击",
   "counter_rate_factor_": "反击率",
   "dodge_rate_": "基础闪避",
   "dodge_rate_factor_": "闪避率",
   "speed_": "基础速度",
   "speed_factor_": "速度",
   "motion_": "基础移动"}

class BattleGroup(object):

    Player = 0
    Enemies = 1
    Friends = 2
    Thirds = 3


class BattlePhase(object):

    Instant = 1
    Start = 2
    StartTurn = 4
    BeforeMove = 8
    AfterMove = 16
    BeforeAttack = 32
    BeforeDamage = 64
    AfterDamage = 128
    AfterAttack = 256
    AfterSettlement = 512
    BeforeItem = 1024
    AfterItem = 2048
    BeforeRest = 4096
    AfterRest = 8192
    FinishTurn = 16384    
    Finish = 32768


class BattleEvent(object):

    HPChanged = 0
    MPChanged = 1
    ACTMissed = 2
    ACTFault = 3
    HPDamaged = 4
    MPDamaged = 5
    PositionMoved = 6
    Counter = 7
    Quit = 8


class EquipPosition(object):

    MainHand = 0
    ViceHand = 1
    Body = 2
    Foot = 3
    Ornament = 4


class SkillStyle(object):

    Boji = "Boji"
    Jianfa = "Jianfa"
    Daofa = "Daofa"
    Changbing = "Changbing"
    Qimen = "Qimen"
    Anqi = "Anqi"


class StatusAcceptType(object):

    Unover = 0
    Different = 1
    Overlap = 2
    

class StatusOverType(object):

    Exert = 0
    Prolong = 1
