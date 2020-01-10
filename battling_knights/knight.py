# Standard Library
import copy

# Local
from .military import Military

SURPRISE_ATTACK = 0.5
KIND_KNIGHT = 'knight'

STATUS_DEAD = 'DEAD'
STATUS_DROWNED = 'DROWNED'
STATUS_LIVE = 'LIVE'


class Knight(Military):
    kind = KIND_KNIGHT
    item = None
    surprise_attack = SURPRISE_ATTACK

    _status = STATUS_LIVE

    def move(self, direction):
        if self.status == STATUS_LIVE:
            super().move(direction)

            if self.status == STATUS_LIVE:
                # add to new field:
                self.board.add(self)

                if self.item:
                    self.item.position = copy.deepcopy(self.position)
                else:
                    self.item = self.board.get_item(self.position)
                    if self.item:
                        self.item.held = True

    @property
    def status(self):
        if self._status == STATUS_LIVE:
            if not self.board.contains(self.position):
                self.drown()
        return self._status

    @property
    def is_live(self):
        return self.status == STATUS_LIVE

    @property
    def attack(self):
        if self.is_live:
            return self.power.attack + self.item_attack + self.surprise_attack

        return 0

    @property
    def base_attack(self):
        if self.is_live:
            return self.power.attack + self.item_attack

        return 0

    @property
    def defence(self):
        if self.is_live:
            return self.power.defence + self.item_defence

        return 0

    @property
    def item_attack(self):
        if self.item:
            return self.item.power.attack

        return 0

    @property
    def item_defence(self):
        if self.item:
            return self.item.power.defence

        return 0

    def get_item(self):
        if self.item:
            return self.item.name

        return None

    def get_position(self):
        if self.is_live:
            return self.position.state()

        return None

    def release_item(self):
        if self.item:
            self.board.add(self.item)
            self.item.held = False
            self.item = None

    def kill(self):
        self.release_item()
        self._status = STATUS_DEAD

    def drown(self):
        self.release_item()
        self._status = STATUS_DROWNED

    def state(self):
        return [
            self.get_position(),
            self.status,
            self.get_item(),
            self.base_attack,
            self.defence,
        ]
