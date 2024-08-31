# This project uses a more object-oriented approach

import pydealer
from pydealer import (Deck, Stack, Card)
from hello import card_numerical_values


class Game:
    def __init__(self):
        self.players = []
        self.centre_stack = Stack()
        self.general_market = Stack()
        self.current_turn_index = 0
        self.winner = None  # the game will keep running till there is a winner

    def is_valid_move(self, card_to_be_played):
        centre_card = self.centre_stack[-1]
        if centre_card.value == card_to_be_played.value or centre_card.suit == card_to_be_played.suit:
            print(card_to_be_played)
            return True
        else:
            return False

    # add a player to the game
    def add_player(self, player_to_be_added):
        player_to_be_added.set_game(self)
        self.players.append(player_to_be_added)

    def create_number_of_players(self, number_of_players):
        for i in range(1, number_of_players + 1):
            self.add_player(Player(i))

    def next_turn(self):
        """Move to the next player's turn."""
        self.current_turn_index = (self.current_turn_index + 1) % len(self.players)

    def get_current_player(self):
        """Return the current player whose turn it is."""
        return self.players[self.current_turn_index]

    def determine_if_winner(self, potential_winner):
        if len(potential_winner.hand) == 0:
            self.winner = potential_winner

    def renew_general_market(self):
        pass

    def play(self):
        while not self.winner:
            current_player = self.get_current_player()
            print("It is ", str(current_player), "'s turn.")

            # player play action
            # either play a card or pick from the general market
            # based on the logic used in line 165 to test
            current_player.take_turn()


            self.determine_if_winner(current_player)
            if self.winner:
                print("The winner is ", current_player)
                break

            self.next_turn()


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

    def get_card(self, card_id):
        for card in self.hand:
            if card.card_id == card_id:
                return card

    def take_turn(self):
        """Define the logic for the player to take a turn."""
        # Example: Play a card from hand, if possible
        # in the full implementation, design the game to make mistakes
        # to let the loss function learn from them
        print('center card: ', self.game.centre_stack[-1], '\n')
        print(self.hand)
        if not len(self.hand) == 0:
            card = self.hand.deal(1)[0]
            if self.game.is_valid_move(card):
                self.play(card)
            else:
                self.hand.add(self.game.general_market.deal(1))
        else:
            print(f"{self.player_id} has no cards to play.")

    def play(self, card_to_be_played):
        self.game.centre_stack.add(
            self.hand.get(card_to_be_played.name)
        )
        # return card_to_be_played

    def pick_from_market(self):
        self.hand.add(self.game.general_market.deal(1))

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


def init_game(game):
    total_deck = HNODeck()
    total_deck.shuffle(3)

    # shuffle the cards and share 5 to each player in the game
    for player in game.players:
        cards = total_deck.deal(5)
        for player_card in cards:
            player.hand.add(player_card)

    # put one card in the playing stack
    game.centre_stack = total_deck.deal(1)
    # put the remaining as the 'general market'
    game.general_market = total_deck


game_1 = Game()
game_1.add_player(Player(1))
game_1.add_player(Player(2))
init_game(game_1)

game_1.play()

# while using reinforcement learning to teach AI to play this game
# a potential issue might arise due to the fact that during a player's turn
# they might pick one or two cards if there are no suitable cards to play
# If the player is aware of the rules of the game and has no cards to play,
# he should pick one card from the general market
#
# However, if the player does not know the rules of the game and erroneously
# plays and inappropriate card, they will be forced to pick two cards
# as a penalty
