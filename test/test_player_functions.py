
from game.Game import Game
from game.utils.models import Player, HNOCard

def test_playing_stack_card_after_dealing():
    game = Game()
    player_1 = Player(1, None)
    
    game.deal_cards_to_players([player_1], 4)
    assert len(player_1.hand) == 4, "There should be 4 cards in the player's hand after dealing."