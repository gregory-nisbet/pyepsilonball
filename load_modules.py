import sys
import os
import math
from pyepsilonball import *

# https://stackoverflow.com/a/246779
try:
    import readline
except ImportError:
    print("Module Readline not available")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")
