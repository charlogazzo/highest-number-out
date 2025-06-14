import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from game.Game import Player
from pydealer import Deck
from game.Game import deal_cards


def test_dealing_of_cards():
    player_1 = Player(1, None)

    deal_cards([player_1])
    print(f"Player 1's hand: {[str(card) for card in player_1.hand]}")
    assert len(player_1.hand) == 5, "Player should have 5 cards in hand after dealing."