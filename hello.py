import pydealer
from pydealer import (Deck, Stack, Card)

deck = pydealer.Deck()
red_joker = Card("Joker", "Red")
black_joker = Card("Joker", "Black")

deck.add(red_joker)
deck.add(black_joker)

for card in deck:
    print(card)
