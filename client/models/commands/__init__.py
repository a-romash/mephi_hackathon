# Удобный импорт всех команд из одного места

from .command import Command
from .move import MoveTo, MoveToRobot
from .tool import ToolRotateTo, ToolVacuumOn, ToolVacuumOff
from .speed import SetMaxSpeed
from .state import GetPosition

__all__ = [
    "Command",
    "MoveTo", "MoveToRobot",
    "ToolRotateTo", "ToolVacuumOn", "ToolVacuumOff",
    "SetMaxSpeed",
    "GetPosition"
]