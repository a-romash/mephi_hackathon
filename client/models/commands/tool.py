# Команды управления инструментом (присоской)

from dataclasses import dataclass
from .command import Command

@dataclass
class ToolRotateTo(Command):
    """
    Повернуть присоску на указанный угол (0-90).
    ВАЖНО: угол абсолютный, а не относительный!
    Пример: 'TOOL_ROTATE_TO 60'
    """
    angle: float

    def to_command(self) -> str:
        return f"TOOL_ROTATE_TO {self.angle}"


@dataclass
class ToolVacuumOn(Command):
    """
    Включить присоску.
    Пример команды: 'TOOL_VACUUM_ON'
    """
    def to_command(self) -> str:
        return "TOOL_VACUUM_ON"


@dataclass
class ToolVacuumOff(Command):
    """
    Выключить присоску.
    Пример команды: 'TOOL_VACUUM_OFF'
    """
    def to_command(self) -> str:
        return "TOOL_VACUUM_OFF"
