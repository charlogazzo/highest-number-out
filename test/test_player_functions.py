
from game.Game import Game
from game.utils.models import Player, HNOCard

def test_playing_stack_card_after_dealing():
    game = Game()
    player_1 = Player(1, None)

    game.assign_players_to_game([player_1])
    game.deal_cards_to_players([player_1], 4)
    assert len(player_1.hand) == 4, "There should be 4 cards in the player's hand after dealing."

def test_stack_updated_after_player_plays_cards():
    # arrange
    game = Game()
    player_1 = Player(1, None)

    game.assign_players_to_game([player_1])
    game.deal_cards_to_players([player_1], 4)
    initial_bottom_card = game.playing_stack.bottom_card

    # act
    cards_to_be_played = player_1.hand[:2]
    player_1.play_cards(cards_to_be_played)

    # assert
    assert initial_bottom_card == game.playing_stack.bottom_card
    assert cards_to_be_played[-1] == game.playing_stack.top_card
    assert len(player_1.hand) == 0

def test_player_pick_card_from_general_market():
    # arrange
    game = Game()
    player_1 = Player(1, None)

    game.assign_players_to_game([player_1])
    game.deal_cards_to_players([player_1], 4)

    # Act
    player_1.pick_card_from_general_market(2)

    # assert
    assert len(player_1.hand) == 6, "The player should have 6 cards in hand after 2 were added to the initial 4"