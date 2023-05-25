"""Common Event attribute types"""

from typing import Literal
from enum import IntEnum


class WorldId(IntEnum):
    connery = 1
    miller = 10
    cobalt = 13
    emerald = 17
    jaeger = 19
    soltech = 40


# TODO: replace with enums
World = Literal[1, 10, 13, 17, 19, 40]
Zone = Literal[2, 4, 6, 8, 344]
