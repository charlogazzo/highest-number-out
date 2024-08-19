# This project uses a more object-oriented approach

import pydealer
from pydealer import (Deck, Stack, Card)
from hello import card_numerical_values


def deal_cards(player_list):
    total_deck = Deck()
    total_deck.shuffle(3)

    for player in player_list:
        cards = total_deck.deal(5)
        for player_card in cards:
            player.hand.append(HNOCard(player_card))
    # shuffle the cards and share 5 to each player in the game


class Game:
    def __init__(self):
        self.players = []
        self.playing_deck = None
        self.market = None
        self.winner = None  # the game will keep running till there is a winner

    """
        see if the bottom card of the stack can be played on the top card
        of the playing deck
    """

    def validate_move(self, played_stack):
        pass

    # add a player to the game
    def add_player(self, player):
        player.set_game(self)
        self.players.append(player)


class HNOCard(Card):
    def __init__(self, card):
        super().__init__(card.value, card.suit)

    @property
    def numerical_value(self):
        return card_numerical_values[self.value]


class Player:
    def __init__(self, player_id, hand):
        self.player_id = player_id
        self.hand = []
        self.game = None

    def set_game(self, game):
        self.game = game

    def play(self):
        pass

    def card_total(self):
        total = 0
        for player_card in self.hand:
            total = total + player_card.numerical_value
        return total

    def check_up(self, game):
        if len(self.hand) == 0:
            game.winner = self

    def __str__(self):
        print("Player ", id)


player_1 = Player(1, None)
player_2 = Player(2, None)

list_of_players = [player_1, player_2]

deal_cards(list_of_players)
for player in list_of_players:
    print(player.card_total())
