MOVES = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}


class Position(object):
    row = None
    column = None

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        return f'{self.__class__.__name__} object: ({self.row}, {self.column})'

    def move(self, direction):
        self.row += MOVES[direction][0]
        self.column += MOVES[direction][1]

    def state(self):
        return [
            self.row,
            self.column,
        ]
