from abc import ABC, abstractmethod


"""
Интерфейс команды для роборуки с методом конвертации её в строку инструкции
"""
class Command(ABC):
    # Конвертирует в строку инструкции
    @abstractmethod
    def to_command() -> str: ...