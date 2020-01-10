# Standard Library
import logging
from collections import OrderedDict

# Local
from .board import Board
from .item import Item
from .knight import Knight

logger = logging.getLogger(__name__)

KNIGHTS = (
    ('R', 'red', 0, 0, 1, 1),
    ('B', 'blue', 7, 0, 1, 1),
    ('G', 'green', 7, 7, 1, 1),
    ('Y', 'yellow', 0, 7, 1, 1),
)
ITEMS = (
    ('M', 'magic_staff', 5, 2, 1, 1),
    ('H', 'helmet', 5, 5, 0, 1),
    ('D', 'dagger', 2, 5, 1, 0),
    ('A', 'axe', 2, 2, 2, 0),
)


class Battle(object):
    knights = None
    items = None
    board = None

    def __init__(self):
        """Setup knights and items on board."""
        self.board = Board(8, 8)
        self.knights = {knight[0]: Knight(self.board, *knight[1:]) for knight in KNIGHTS}
        self.items = {item[0]: Item(self.board, *item[1:]) for item in ITEMS}

    def print_board(self, separator='*'):  # to remove
        print('***', separator, '***')
        for r_num, row in self.board.fields.items():
            for c_num, column in row.items():
                print(r_num, c_num, self.board.fields[r_num][c_num].__dict__)

    def move_knight(self, knight, direction):
        self.board.move(self.knights[knight], direction)

    def state_by_kind(self, kind, attr_name):
        return {row[1]: getattr(self, attr_name)[row[0]].state() for row in kind}

    def state(self):
        data = OrderedDict()
        data.update(self.state_by_kind(KNIGHTS, 'knights'))
        data.update(self.state_by_kind(ITEMS, 'items'))

        return data

    def knights_report(self):
        report = ''
        for knight in self.knights.values():
            name = knight.name
            if knight.is_live:
                name = name.upper()
            report += (
                f'{name:10s}| pow: ({knight.base_attack, knight.defence}), '
                f'pos: {knight.position.state()}, status: {knight.status}\n'
            )
        return report
