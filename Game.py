class Game:
    def __init__(self):
        self.players = []
        self.playing_deck = None
        self.market = None


class Player:
    def __init__(self, id, hand):
        self.id = id
        self.hand = hand

    def __str__(self):
        print("Player ", id)
