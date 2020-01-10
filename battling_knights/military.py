# Local
from .position import Position
from .power import Power


class Military(object):
    board = None
    name = None
    kind = None
    position = None
    power = None

    def __init__(self, board, name, row, column, attack, defence):
        self.name = name
        self.power = Power(attack, defence)
        self.position = Position(row, column)

        self.board = board
        self.board.add(self)

    def __repr__(self):
        return (
            f'{self.__class__.__name__} object: '
            f'{self.name}({self.attack}, {self.defence})'
        )

    @property
    def attack(self):
        return self.power.attack

    @property
    def defence(self):
        return self.power.defence

    def get_position(self):
        return self.position.state()

    def move(self, direction):
        self.position.move(direction)

    def state(self):
        NotImplementedError()
