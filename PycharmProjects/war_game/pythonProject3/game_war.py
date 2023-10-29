from deck_cards import Deck
from player import Player
from card_game import Card


def winner(card_1, card_2):
    if card_1 > (card_2):
        return 'player_1'
    elif card_1 < (card_2):
        return 'player_2'
    else:
        return 'equal'


class Game:
    def __init__(self, num_players):
        self.deck_cards = Deck()
        self.deck_cards.shuffle()
        self.players = [Player(f'player{p}', hand=[], idx=p) for p in range(num_players)]
        while len(self.deck_cards) > 0:
            for player in self.players:
                if len(self.deck_cards) > 0:
                    player.hand.append(self.deck_cards.draw)
        self.start_game()

    def start_game(self):
        self.play_round()

    def play_round(self):
        round_cards = [[] * num_players]
        for player in self.players:
            round_cards[player.idx].append(player.draw())
        max_card = max([round_cards[- 1]])
        war_players = []
        for player in self.playeres:
            if round_cards[player.idx][- 1] == max_card:
                war_players.append(player.idx)
        if len(war_players) > 1:
            self.is_a_war()

    #         
    # def is_a_war(self, war_players):
    #     for player in war_players:
    #


            # round_cards.append(player.draw)



        # war_cards_round = []
        # if war_cards is not None:
        # war_cards_round.append(war_cards)
        card_1 = self.hand_1.pop()
        card_2 = self.hand_2.pop()
        win = winner(card_1, card_2)
        if win == 'player_1':
            hand_1.append(card_1), hand_1.append(card_2), hand_1.append(war_cards_round)
            self.win_1 += 1
        elif win == 'player_2':
            hand_2.append(card_1), hand_2.append(card_2), hand_2.append(war_cards_round)
            self.win_2 += 1
        elif win == 'equal':
            war_cards_round.append(card_1)
            war_cards_round.append(card_2)
            for i in range(3):
                if len(self.hand_1) > 0:
                    war_cards_round.append(self.hand_1.pop())
                if len(self.hand_2) > 0:
                    war_cards_round.append(self.hand_2.pop())
            play_round(war_cards=war_cards_round)

# a = Game(3)
# print(a.deck_cards.deck)
# print(a.hand)
