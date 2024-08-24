# This project uses a more object-oriented approach

import pydealer
from pydealer import (Deck, Stack, Card)
from hello import card_numerical_values


class Game:
    def __init__(self):
        self.players = []
        self.centre_stack = Stack()
        self.general_market = Stack()
        self.winner = None  # the game will keep running till there is a winner

    """
        see if the bottom card of the stack can be played on the top card
        of the playing deck
    """
    def is_valid_move(self, card_to_be_played):
        centre_card = self.centre_stack[-1]
        if centre_card.value == card_to_be_played.value or centre_card.suit == card_to_be_played.suit:
            print(card_to_be_played)
            return True
        return False

    # add a player to the game
    def add_player(self, player_to_be_added):
        player_to_be_added.set_game(self)
        self.players.append(player_to_be_added)

    def get_player_with_smallest_hand(self):
        """Return the player with the smallest hand size."""
        if not self.players:
            return None  # No players in the game

        # Start by assuming the first player has the smallest hand
        smallest_hand_player = self.players[0]

        for current_player in self.players[1:]:
            if len(current_player.hand) < len(smallest_hand_player.hand):
                smallest_hand_player = current_player

        return smallest_hand_player


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

    def play(self, card_to_be_played):
        self.game.centre_stack.add(
            self.hand.get(card_to_be_played.name)
        )

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


def init_game(player_list, game):
    total_deck = HNODeck()
    total_deck.shuffle(3)

    # shuffle the cards and share 5 to each player in the game
    for player in player_list:
        game.add_player(player)
        cards = total_deck.deal(5)
        for player_card in cards:
            player.hand.add(player_card)

    # put one card in the playing stack
    game.centre_stack = total_deck.deal(1)
    # put the remaining as the 'general market'
    game.general_market = total_deck


# instantiate players
player_1 = Player(1)
player_2 = Player(2)

list_of_players = [player_1, player_2]

# create a game and add players to it
game_1 = Game()
init_game(list_of_players, game_1)

move_count = 0

print('size of centre stack at start of the game', len(game_1.centre_stack))

while game_1.winner is None:
    for player in game_1.players:
        for card in player.hand:
            # actually, the player should play the card before the move is validated
            # this will allow the game to penalize if the move is illegal
            if game_1.is_valid_move(card):
                print('Valid move: ', str(card))
                player.play(card)
                # break out of this after playing the card so that the next player plays

    game_1.winner = game_1.get_player_with_smallest_hand()
    print(game_1.winner)

print('size of centre stack at end of the game', len(game_1.centre_stack))
print('length of player 1\'s hand', len(player_1.hand))
print('length of player 2\'s hand', len(player_2.hand))
