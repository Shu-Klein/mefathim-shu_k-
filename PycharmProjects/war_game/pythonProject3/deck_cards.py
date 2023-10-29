import random
from card_game import Card, Suits, Ranks


class Deck:
    def __init__(self, joker=False):
        self.deck = []
        for s in Suits:
            for r in Ranks:
                if s.value != "X_joker" and r.value != 15:
                    self.deck.append(Card(s, r))
                elif s.value == "X_joker" and r.value == 15 and joker is True:
                    self.deck.append(Card(s, r))
                    self.deck.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, item):
        if 0 <= item <= len(self.deck):
            return self.deck[item]
        raise "item is not in the deck"

    def sort_by_suit(self):
        self.deck.sort(key=lambda card: (card.suit.value, card.rank.value))

    def sort_by_rank(self):
        self.deck.sort(key=lambda card: (card.rank.value, card.suit.value))

    def deal_hand(self, num_hand):
        list_hand = []
        for i in range(num_hand):
            list_hand.append(self.draw())
        return list_hand

    def count_cards(self):
        instances = {"Ranks.TOO_2": 0, "Ranks.TREE_3": 0, "Ranks.FOUR_4": 0, "Ranks.FIVE_5": 0, "Ranks.SIX_6": 0,
                     "Ranks.SEVEN_7": 0, "Ranks.EIGHT_8": 0, "Ranks.NINE_9": 0, "Ranks.TEN_10": 0, "Ranks.JACK": 0,
                     "Ranks.QUEEN": 0, "Ranks.KING": 0, "Ranks.ACE": 0, "Ranks.JOKER": 0}
        for card in self.deck:
            str_card = str(card.rank)
            instances[str_card] += 1
        return instances

# deck_cards = Deck()
# print(deck_cards.deck)
# deck_cards.shuffle()
# print(deck_cards.deck)
# deck_cards.sort_by_rank()
# print(deck_cards.deck)
# print(deck_cards.deal_hand(3))
# print(deck_cards.count_cards())
