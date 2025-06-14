import pydealer
from pydealer import (Deck, Stack, Card)

card_numerical_values = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Joker": 20
}

deck = pydealer.Deck()
red_joker = Card("Ace", "Spades")
black_joker = Card("Ace", "Spades")
