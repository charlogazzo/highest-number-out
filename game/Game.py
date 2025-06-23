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

    def assign_players_to_game(self, players_list):
        # Assign the list of players to the game
        self.players = players_list
        for player in self.players:
            player.set_game(self)

        # set the next player of each player in the game
        if len(players_list) > 2:
            for index in range(1, len(players_list)):
                players_list[index - 1].next_player = players_list[index]
            players_list[-1].next_player = players_list[0]

    def deal_cards_to_players(self, player_list, num_cards):
        total_deck = self.game_deck
        total_deck.shuffle(3)

        # Deal 5 cards to each player
        for player in player_list:
            cards = total_deck.deal(num=num_cards)
            # print(cards.cards)
            for player_card in cards:
                player.hand.append(player_card)
        
        # Deal 1 card to the playing stack
        if len(total_deck.cards) > 0:
            self.playing_stack = total_deck.deal(1)

        print("playing stack after dealing: ", self.playing_stack)

        # the rest of the deck goes to the general market
        self.general_market = Stack(cards=list(total_deck.cards))

    # For a stack of more than one card being played, the first validation should be that the bottom card matches
    # the current top card of the playing stack.
    # If that is true then check all the cards to see that they have an equal value
    def check_cards_being_played(self, card_stack_to_be_played: HNOStack):
        cards = card_stack_to_be_played.cards
        if cards[0].suit != self.playing_stack.top_card.suit or cards[0].value != self.playing_stack.top_card.value:
            raise Exception("The bottom card does not match the top card of the playing stack")
        if len(cards) > 1:
            value_set = set()
            for card in cards:
                value_set.add(card.value)
            if len(value_set) > 1:
                raise Exception("An invalid stack of cards was played. There is more than one value in the stack")





player_1 = Player(1, None)
player_2 = Player(2, None)

list_of_players = [player_1, player_2]

game = Game()
game.deal_cards_to_players(list_of_players, 5)

deck = Deck()
print([str(card) for card in deck.cards])

