import importlib

scripts = importlib.import_module("%s.scripts" % __name__, package="proj.modules")
info = importlib.import_module("%s.info" % __name__, package="proj.modules")
