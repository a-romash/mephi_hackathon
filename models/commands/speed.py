# Команда установки максимальной скорости

from dataclasses import dataclass
from .command import Command

@dataclass
class SetMaxSpeed(Command):
    """
    Установить максимальные скорости по осям X Y Z (мм/с).
    Пример: 'SET_MAX_SPEED 1500 1500 1500'
    """
    x_speed: int
    y_speed: int
    z_speed: int

    def to_command(self) -> str:
        return f"SET_MAX_SPEED {self.x_speed} {self.y_speed} {self.z_speed}"
