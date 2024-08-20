# This project uses a more object-oriented approach

import pydealer
from pydealer import (Deck, Stack, Card)
from hello import card_numerical_values


def init_game(player_list, game):
    total_deck = HNODeck()
    total_deck.shuffle(3)

    # shuffle the cards and share 5 to each player in the game
    for player in player_list:
        cards = total_deck.deal(5)
        for player_card in cards:
            player.hand.add(player_card)

    # put one card in the playing stack
    game.playing_stack = total_deck.deal(1)
    # put the remaining as the 'general market'
    game.market = total_deck


class Game:
    def __init__(self):
        self.players = []
        self.playing_stack = Stack()
        self.market = Stack()
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
    def __init__(self, card, card_id):
        super().__init__(card.value, card.suit)
        self.card_id = card_id

    @property
    def numerical_value(self):
        return card_numerical_values[self.value]

    def __str__(self):
        return super().__str__() + " | id: " + str(self.card_id)


class HNODeck(Deck):

    def __init__(self):
        super().__init__()

        # convert the cards to HNOCards
        default_cards = self.empty(return_cards=True)
        temp_hno_deck = [HNOCard(card, card_id) for card_id, card in enumerate(
            default_cards, start=1
        )]
        self.set_cards(temp_hno_deck)


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = Stack()
        self.game = None

    def set_game(self, game):
        self.game = game

    # TODO: get card instance
    # def getCard(self, card_id):
    #     for card in self.hand:
    #         if card.card_id == card_id:
    #             return card

    def play(self, card_id):
        current_playing_stack = self.game.playing_stack

        # TODO: add card to the playing stack from getCard method
        current_playing_stack.add()

        # the stack that will leave the player's hand and
        # be played on the playing stack

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
        return "Player " + str(self.player_id)


player_1 = Player(1)
player_2 = Player(2)

list_of_players = [player_1, player_2]

game_1 = Game()
game_1.players = list_of_players
init_game(list_of_players, game_1)

[print(card) for card in player_2.hand]
print(game_1.playing_stack)
