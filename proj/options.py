# -- coding: utf-8 --

# ----------------------------------------------
# |                  基本选项                  |
# ----------------------------------------------

# 游戏数据目录
DATA_PATH = "proj.data"

# 是否使用多线程
MULTIPLE_THREAD = True

# ----------------------------------------------
# |                  战斗选项                  |
# ----------------------------------------------

# 战斗地图的最大尺寸，与屏幕分辨率、控制台大小相关，若机器屏幕小可以设小点，尤其是宽度
MAP_MAX_WIDTH = 8
MAP_MAX_HEIGHT = 10

# 战斗地图是否允许采用镜头模式（暂不建议使用）
USE_CAMERA_MODE = True
CAMERA_WINDOW_WIDTH = 8
CAMERA_WINDOW_HEIGHT = 9

# 单次战斗主战方最大上场人数 
BATTLE_MAX_PEOPLE_MAIN = 6

# 单次战斗援助方最大上场人数
BATTLE_MAX_PEOPLE_SUPPORT = 3

# 是否允许控制队伍中除自己以外的成员
CAN_CONTROL_MEMBER = True

# 指定NPC使用的AI脚本
USE_AI = "proj.ai.simple.SimpleAI"

# 自动战斗是否播放战斗过程
PLAY_AUTO_BATTLE = False

# ----------------------------------------------
# |                  界面选项                  |
# ----------------------------------------------

# 控制台字体是否不会对全角字符进行显示优化（除lucida console外基本都为True）
USE_FULL_WIDTH_FONT = False

# ----------------------------------------------
# |                  场景选项                  |
# ----------------------------------------------

# 大地图玩家一次最多行走的步数（建议设置为地图窗口长宽的一半以下）
MOTION_SCENARIO = 3
