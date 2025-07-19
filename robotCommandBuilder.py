from models.arUcoTile import ArUcoTile
from models.commands import Command, MoveTo, ToolVacuumOn, ToolVacuumOff, ToolRotateTo

"""
Введём следующие предположения:
    1. Лишние тайлы размером 80x80x4мм
    2. Угол тайлов -- наименьший угол, на который надо повернуть тайл, чтобы его стороны стали параллельны осям плоскости
"""

def solve(tiles_to_remove: list[ArUcoTile], tiles_to_build: list[ArUcoTile], x_pyramid: float, y_pyramid: float) -> list[Command]:
    """
    Description:
        Решает задачу по генерации команд для роборуки
    
    Attributes:
        tiles_to_remove: list[ArUcoTile] - тайлы, которые не требуются для построения пирамиды
        tilesToBuild: list[ArUcoTile] - тайлы, из которых необходимо строить пирамиду
        x_pyramid, y_pyramid: float - координаты, где необходимо построить пирамиду
    
    Returns:
        list[Command] - список команд для роборуки
    """

    """
    План действий:
        0. Убираем ненужные тайлы
        1. Проверяем, свободно ли поле для построения пирамидки
        2. Убираем лишние тайлы, если нет
        3. Строим пирамидку
    """

    commands: list[Command] = []

    commands += remove(tiles_to_remove)



def check_field(tiles: list[ArUcoTile], x_pyramid: float, y_pyramid: float, size: int) -> list[ArUcoTile]:
    """
    Description: 
        Проверяет площадку для строительства на наличие тайлов, которые будут мешать постройке пирамиды

    Attributes:
        tiles: list[ArUcoTile] - все тайлы на плоскости
        x_pyramid, y_pyramid: float - координаты, где необходимо построить пирамиду
        size: int - размер площади, где надо построить пирамиду (с которой надо убрать тайлы)
    
    Returns:
        list[ArUcoTile] - список тайлов, которые лежат на площадке и мешают
    """
    
    half_size = size / 2
    min_x = x_pyramid - half_size
    max_x = x_pyramid + half_size
    min_y = y_pyramid - half_size
    max_y = y_pyramid + half_size

    to_remove = []
    for tile in tiles:
        if min_x <= tile.x <= max_x and min_y <= tile.y <= max_y:
            to_remove.append(tile)

    return to_remove


def remove(tiles: list[ArUcoTile]) -> list[Command]:
    """
    Description:
        Генерирует последовательность команд для удаления тайлов с плоскости.
        Каждый тайл поднимается с помощью присоски и переносится за пределы поля (например, на координаты (330, 330)).

    Attributes:
        tiles: list[ArUcoTile] - список тайлов, которые нужно убрать с плоскости

    Returns:
        list[Command] - список команд, необходимых для удаления всех указанных тайлов
    """

    commands: list[Command] = []

    # Начальная высота над тайлом (для безопасного перемещения)
    Z_ABOVE = 100.0

    # Высота для захвата тайла
    Z_PICK = 4.0

    # Координаты зоны сброса (вне основной области 300x300)
    DROP_X, DROP_Y = 330, 330
    Z_DROP = 9.0

    for tile in tiles:
        # Подлететь сверху
        commands.append(MoveTo(tile.x, tile.y, Z_ABOVE))
        
        # Снизиться и схватить тайл
        commands.append(MoveTo(tile.x, tile.y, Z_PICK))
        commands.append(ToolVacuumOn())

        # Подняться
        commands.append(MoveTo(tile.x, tile.y, Z_ABOVE))

        # Перелететь в зону сброса
        commands.append(MoveTo(DROP_X, DROP_Y, Z_ABOVE))
        commands.append(MoveTo(DROP_X, DROP_Y, Z_DROP))

        # Отпустить тайл
        commands.append(ToolVacuumOff())

        # Подняться снова
        commands.append(MoveTo(DROP_X, DROP_Y, Z_ABOVE))

    return commands