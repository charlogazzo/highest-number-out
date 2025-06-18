import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from game.Game import Player, Game
from pydealer import Deck


def test_dealing_of_cards():
    game = Game()
    player_1 = Player(1, None)

    game.deal_cards([player_1])
    assert len(player_1.hand) == 5, "Player should have 5 cards in hand after dealing."

def test_players_added_to_game():
    game = Game()
    player_1 = Player(1, None)
    player_2 = Player(2, None)

    game.deal_cards([player_1, player_2])
    assert len(game.players) == 2, "Game should have 2 players after dealing cards."

def test_played_cards_match_top_of_playing_stack():
    game = Game()
    player_1 = Player(1, None)
    
    game.deal_cards([player_1])
    assert len(game.playing_stack) == 1, "There should be one card in the playing stack after dealing."

def test_general_market_initialization_after_dealing_cards():
    game = Game()
    player_1 = Player(1, None)
    player_2 = Player(2, None)
    game.deal_cards([player_1, player_2])

    assert len(game.general_market) == 43, "General market should have 43 cards after dealing 10 cards to players and 1 in the playing stack (54 - 5*2 -1 = 43)."
    
