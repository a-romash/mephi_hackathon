# Команда получения текущей позиции робота

from dataclasses import dataclass
from .command import Command

@dataclass
class GetPosition(Command):
    """
    Получить текущую позицию робота.
    Пример команды: 'GET_POSITION'
    """
    def to_command(self) -> str:
        return "GET_POSITION"
