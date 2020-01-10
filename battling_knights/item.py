# Local
from .military import Military

KIND_ITEM = 'item'

PRIORITIES = {
    'axe': 0,
    'magic_staff': 1,
    'dagger': 2,
    'helmet': 3,
}


class Item(Military):
    kind = 'item'
    is_held = False

    @property
    def priority(self):
        return PRIORITIES[self.name]

    def state(self):
        return [
            self.position.state(),
            self.is_held
        ]
