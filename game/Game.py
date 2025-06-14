# This project uses a more object-oriented approach

import pydealer
from pydealer import (Deck, Stack, Card)
from game.hello import card_numerical_values


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


class HNOCard(Card):
    def __init__(self, card):
        super().__init__(card.value, card.suit)

    @property
    def numerical_value(self):
        return card_numerical_values[self.value]
    
    ### Override the __str__ method to return a string representation of the card
    # TODO: Find out why the super class __str__ is being called instead of this one
    def __str__(self):
        return f"{self.value} of {self.suit} (value: {self.numerical_value})"


class Player:
    def __init__(self, player_id, hand):
        self.player_id = player_id
        self.hand = []
        self.game = None

    def set_game(self, game):
        self.game = game

    def __str__(self):
        print("Player ", id)


player_1 = Player(1, None)
player_2 = Player(2, None)

list_of_players = [player_1, player_2]

deck = Deck()
hno_card = HNOCard(deck.deal(1)[0])
print(hno_card)  # This will call the __str__ method of HNOCard