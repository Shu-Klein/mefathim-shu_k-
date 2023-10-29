from enum import Enum


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank


class Ranks(Enum):
    TOO_2 = 2
    TREE_3 = 3
    FOUR_4 = 4
    FIVE_5 = 5
    SIX_6 = 6
    SEVEN_7 = 7
    EIGHT_8 = 8
    NINE_9 = 9
    TEN_10 = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    JOKER = 15


class Suits(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'
    JOKER = 'X_joker'


