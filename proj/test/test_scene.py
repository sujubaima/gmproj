import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../"))

from proj.console import interscene as interscn

if __name__ == "__main__":
    interscn.scene()
