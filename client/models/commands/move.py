# Команды перемещения робота

from dataclasses import dataclass
from .command import Command

@dataclass
class MoveTo(Command):
    """
    Перемещение в координатах ПОЛЯ (field).
    Пример команды: 'MOVE_TO 270 200 200'
    """
    x: float
    y: float
    z: float

    def to_command(self) -> str:
        return f"MOVE_TO {self.x} {self.y} {self.z}"


@dataclass
class MoveToRobot(Command):
    """
    Перемещение в координатах РОБОТА.
    Пример команды: 'MOVE_TO_ROBOT 350 80 200'
    """
    x: float
    y: float
    z: float

    def to_command(self) -> str:
        return f"MOVE_TO_ROBOT {self.x} {self.y} {self.z}"
