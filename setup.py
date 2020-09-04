import site
from shutil import copyfile

from compatibility import slash_type as s

copyfile("switch.py", site.getsitepackages()[0] + s())
