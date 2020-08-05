import importlib

from proj import options

superskill = importlib.import_module("%s.superskills" % options.DATA_PATH)
person = importlib.import_module("%s.persons" % options.DATA_PATH)
skill = importlib.import_module("%s.skills" % options.DATA_PATH)
status = importlib.import_module("%s.status" % options.DATA_PATH)
effect = importlib.import_module("%s.effects" % options.DATA_PATH)
item = importlib.import_module("%s.items" % options.DATA_PATH)
recipe = importlib.import_module("%s.recipes" % options.DATA_PATH)
map = importlib.import_module("%s.maps" % options.DATA_PATH)
terran = importlib.import_module("%s.terrans" % options.DATA_PATH)
element = importlib.import_module("%s.elements" % options.DATA_PATH)
event = importlib.import_module("%s.events" % options.DATA_PATH)
discovery = importlib.import_module("%s.discoveries" % options.DATA_PATH)
task = importlib.import_module("%s.tasks" % options.DATA_PATH)
scripts = importlib.import_module("%s.scripts" % options.DATA_PATH)
force = importlib.import_module("%s.forces" % options.DATA_PATH)

