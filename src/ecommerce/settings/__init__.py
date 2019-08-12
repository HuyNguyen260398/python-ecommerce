from .base import *  # import all

from .production import *

try:
    from .local import *
except:
    pass
