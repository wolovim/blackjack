from game import Game
from deck import Deck

suits = ['C', 'H', 'S', 'D']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def display_player_hand(hand):
  return "{card_1}, {card_2}".format(card_1=hand[0], card_2=hand[1])

def display_dealer_hand(hand):
  return "{card_1}, HIDDEN".format(card_1=hand[0])

print "Blackjack!"
game = Game()

while game.chips > 0:
  deck = Deck(suits, ranks)

  player_hand = deck.deal()
  dealer_hand = deck.deal()

  print "\nYou have {chips} chips.".format(chips=game.chips)
  bet = int(raw_input("How many would you like to bet? "))

  print "\nYour hand: {hand}".format(hand=display_player_hand(player_hand))
  print "Dealer's hand: {hand}\n".format(hand=display_dealer_hand(dealer_hand))

  while True:
    input = raw_input('Want to (h)it or (s)tay? ')

    if input == 'h':
      print 'hitting!'
    elif input == 's':
      outcome = game.evaluate_round(player_hand, dealer_hand)
      print outcome
      game.win_chips(bet) if outcome == 'win!' else game.lose_chips(bet)
      break
    else:
      continue

else:
  print "\nOut of chips!\nGame over!"
