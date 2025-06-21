# This project uses a more object-oriented approach

import pydealer
from pydealer import (Deck, Stack, Card)
from game.utils.models import HNOCard, Player, HNODeck, HNOStack


class Game:
    def __init__(self):
        self.players = []
        self.game_deck = HNODeck()
        self.playing_stack = HNOStack(cards=None)
        self.general_market = HNOStack(cards=None)

    def deal_cards_to_players(self, player_list, num_cards):
        total_deck = self.game_deck
        total_deck.shuffle(3)

        # Deal 5 cards to each player
        for player in player_list:
            cards = total_deck.deal(num=num_cards)
            print(cards.cards)
            for player_card in cards:
                player.hand.append(player_card)

        # Assign the list of players to the game
        self.players = player_list
        for player in self.players:
            player.set_game(self)
        
        # Deal 1 card to the playing stack
        if len(total_deck.cards) > 0:
            self.playing_stack = total_deck.deal(1)

        # the rest of the deck goes to the general market
        self.general_market = Stack(cards=list(total_deck.cards))


player_1 = Player(1, None)
player_2 = Player(2, None)

list_of_players = [player_1, player_2]

game = Game()
game.deal_cards_to_players(list_of_players, 5)

