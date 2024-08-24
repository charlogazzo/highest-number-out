from pydealer import Stack, Card
from Game import HNODeck, HNOCard
from pydealer.const import BOTTOM, TOP

deck = HNODeck()
stack = Stack()

deck.shuffle(3)

card_1 = Card("2", "Spades")
card_2 = Card("2", "Hearts")
card_3 = Card("2", "Clubs")
card_4 = Card("2", "Diamonds")

stack.add(HNOCard(card_1, 1))
stack.add(HNOCard(card_2, 2))
stack.add(HNOCard(card_3, 3), end=TOP)
stack.add(HNOCard(card_4, 4), end=BOTTOM)

# print(stack[0])  # 2 of diamonds
# print(stack[-1])  # 2 of clubs

# from this experiment, we see that a card inserted at the top of a stack
# is accessed by retrieving the final index of the stack.
# this is similar to a card placed at the bottom of the stack,
# it is accessed by retrieving index 0 from the stack


centre_cards = deck.deal(10)
general_market = Stack()

print('Top of the centre cards: ', centre_cards[-1])

for card_position in range(-1, -(len(deck)), -1):
    topmost_card = centre_cards[-1]
    card_to_be_played = deck.deal(1)[-1]
    if topmost_card.value == card_to_be_played.value or topmost_card.suit == card_to_be_played.suit:
        print(card_to_be_played)
        break
    else:
        general_market.add(card_to_be_played)

print('general market size: ', len(general_market))

