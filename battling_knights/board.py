# Standard Library
import heapq

# Local
from .item import KIND_ITEM
from .knight import KIND_KNIGHT
from .position import Position


class Field(object):
    items = None
    knight = None
    position = None

    def __init__(self, row, column):
        self.position = Position(row, column)
        self.items = []

    def add(self, military):
        if military.kind == KIND_ITEM:
            self.add_item(military)

        if military.kind == KIND_KNIGHT:
            self.knight = self.fight(military)

    def add_item(self, item):
        """Add item regarding to order."""
        heapq.heappush(self.items, (item.priority, item))

    def fight(self, military):
        # what is looser item logic?
        if self.knight:
            if self.knight.defence > military.attack:
                military.kill()
                return self.knight
            else:
                self.knight.kill()

        return military

    def get_item(self):
        try:
            return heapq.heappop(self.items)[1]
        except IndexError:
            pass

        return None

    def release(self, military):
        if military.kind == KIND_ITEM:
            self.items.remove(military)

        if military.kind == KIND_KNIGHT:
            self.knight = None


class Board(object):
    fields = None
    rows = None
    columns = None

    def __init__(self, rows, columns):
        self.fields = {}
        self.rows = rows
        self.columns = columns

    def _get_field(self, position):
        return self.fields[position.row][position.column]

    def add(self, military):
        """Add new military to board."""
        row = military.position.row
        column = military.position.column
        try:
            field = self.fields[row][column]
        except KeyError:
            field = self.fields.setdefault(row, {})[column] = Field(row, column)

        field.add(military)
        return field

    def contains(self, position):
        """Is position on board?"""
        return self.rows > position.row >= 0 and self.columns > position.column >= 0

    def get_item(self, position):
        return self._get_field(position).get_item()

    def move(self, knight, direction):
        """Move military regarding to direction."""
        # release old field:
        if knight.is_live:
            self._get_field(knight.position).release(knight)
            # move military:
            knight.move(direction)

    def draw(self):
        board = ''
        board += '    |'
        for column in range(self.columns):
            board += f'{column:5d}|'
        board += '\n'

        for row in range(self.rows):
            board += ((self.columns + 1) * 6 * '-') + '\n'
            board += f'{row:5d}|'
            for column in range(self.columns):
                try:
                    field = self._get_field(Position(row, column))
                    info = ''
                    if field.knight:
                        if field.knight.is_live:
                            info += field.knight.name[0].upper()
                        else:
                            info += field.knight.name[0]

                        if field.knight.item:
                            info += field.knight.item.name[0]

                        info += ' '
                    if field.items:
                        for item in field.items:
                            info += item[1].name[0].upper()
                except KeyError:
                    info = ''
                board += f'{info:5s}|'
            board += '\n'

        return board
