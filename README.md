# highest-number-out
A python implementation of the card game called Highest Number Out

The aim is to have the lowest total of card numbers at the end of the game.

The player that wins the game has the no cards in the hand because he has "checked up".
The loser is the player whose card total is the highest

Obviously, not all cards in a standard deck have numerical values, so we will assign values to them

Needless to say, cards 2-9 retain their values when calculating totals in game

| Card  | Numerical Value in Game |
|-------|-------------------------|
| Ace   | 1                       |
| Jack  | 11                      |
| Queen | 12                      |
| King  | 13                      |
| Joker | 20                      |

Action Cards
There are cards that when placed by a user onto the playing deck, demand that an extra action is taken

| Card  | Action         | Description                                                |
|-------|----------------|------------------------------------------------------------|
| 1     | Hold-on        | The player may place any Suit on top of this card          |
| 2     | Pick Two       | The next player should pick two cards                      |
| 5     | Pick Three     | The next player should pick three cards                    |
| 7     | Block          | This is used to block a "Pick Two" or "Pick Three"         |
| 8     | Suspension     | The next player misses their turn                          |
| Jack  | General Market | Every player picks a card                                  |
| Joker | "I need"       | The player requests a suit to be played. It must be played |
|       |                | The Joker also blocks "Pick Two" and "Pick Three"          |


# how it's played

A number of cards (usually between 4 and 7) are dealt to each player at the start of the game
and a card (a non-action card) is placed in the middle to start.

The Golden Rule:
The next player must then play a card that has a similar number or suit to the current card at the top

A player may legally play more than one card if:
1. They are same number
2. The card at the bottom of the stack he places on the playing fulfils the golden rule

If the player makes a mistake, they have to pick two cards and a penalty
