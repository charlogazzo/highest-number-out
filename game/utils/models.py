from pydealer import Card, Stack, Deck, TOP
from game.hello import card_numerical_values

"""
Implementation of the Pydealer deck to fit the requirements of the HNO Game

This has two jokers added to the deck and each card in the deck cast as a HNOCard
"""
class HNODeck(Deck):
    def __init__(self, **kwargs):
        super().__init__(num_jokers=2, jokers=True)
        self.cards = [HNOCard(card) for card in self.cards]

    def deal(self, num=1, rebuild=False, shuffle=False, end=TOP):
        return HNOStack(cards=list(super().deal(num, rebuild, shuffle, end).cards))


class HNOStack:
    def __init__(self, cards):
        self.cards = [] or cards

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    @property
    def top_card(self):
        return self.cards[len(self.cards) - 1]

    @property
    def bottom_card(self):
        return self.cards[0]

    def add(self, cards):
        self.cards.extend(cards)


class HNOCard(Card):
    def __init__(self, card):
        super().__init__(card.value, card.suit)

    @property
    def numerical_value(self):
        return card_numerical_values[self.value]

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.abbrev} (value: {self.numerical_value})"


class Player:
    def __init__(self, player_id, hand):
        self.player_id = player_id
        self.hand = []
        self.game = None

    def set_game(self, game):
        self.game = game

    def show_player_hand(self):
        return [str(card.abbrev) for card in self.hand]

    def play_cards(self, cards):
        stack_to_be_played = HNOStack()
        for card in cards:
            if card in self.hand:
                stack_to_be_played.add(card)
                self.hand.remove(card)

    def __str__(self):
        print("Player ", id)