import random


class Player:
    def __init__(self, name, hand: list, idx):
        self.name = name
        self.hand = hand
        self.round_hand = []
        self.idx = idx

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == str(name):
            self._name = name

    def draw(self):
        if len(hand) > 0:
            return self.hand.pop()

    def shuffle(self):
        if len(self.hand) > 1:
            random.shuffle(self.hand)

