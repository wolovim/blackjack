from game import Game
from deck import Deck
from hand import Hand

def display_player_hand(hand):
  return "{card_1}, {card_2}".format(card_1=hand[0], card_2=hand[1])

def display_dealer_hand(hand):
  return "{card_1}, HIDDEN".format(card_1=hand[0])

print "Blackjack!"
game = Game()

while game.chips > 0:
  deck = Deck()

  player_hand = Hand()
  deck.deal(player_hand)

  dealer_hand = Hand()
  deck.deal(dealer_hand)

  # Get player bet
  while True:
    try:
      print "\nYou have {chips} chips.".format(chips=game.chips)
      bet = int(raw_input("How many would you like to bet? "))
      if bet > game.chips:
        print "You can't bet more than you have!"
        continue
      else:
        break
    except:
      print "\nPlease enter a number of chips!"

  # Show the field
  print "\nYour hand: {hand}".format(hand=display_player_hand(player_hand.cards))
  print "Dealer's hand: {hand}\n".format(hand=display_dealer_hand(dealer_hand.cards))

  # Prompt user user action: hit or stay
  while True:
    input = raw_input('Want to (h)it or (s)tay? ')

    if input == 'h':
      print 'hitting!'
      deck.hit(player_hand)
    elif input == 's':
      game.evaluate_round(bet, player_hand.cards, dealer_hand.cards)
      break
    else:
      print "\nGotta enter 'h' or 's'!"
      continue

else:
  print "\nOut of chips!\nGame over!"
