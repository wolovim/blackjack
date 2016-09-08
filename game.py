from deck import Deck

suits = ['C', 'H', 'S', 'D']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values = { 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

def hand_value(hand):
  value = 0
  for card in hand:
    value += values[card[1:]]
  return value

chips = 100
deck = Deck(suits, ranks)

player_hand = deck.deal()
dealer_hand = deck.deal()

def display_player_hand(hand):
  return "{card_1}, {card_2}".format(card_1=hand[0], card_2=hand[1])

def display_dealer_hand(hand):
  return "{card_1}, HIDDEN".format(card_1=hand[0])

print "Blackjack!"
while chips > 0:
  print "\nYou have {chips} chips.".format(chips=chips)
  bet = int(raw_input("What would you like to bet? "))
  print "Your hand is: {hand}. Value is: {value}".format(hand=display_player_hand(player_hand), value=hand_value(player_hand))
  print "Dealer's hand is: {hand}. Value is: {value}".format(hand=display_dealer_hand(dealer_hand), value=hand_value(dealer_hand))
  chips -= bet
else:
  print "\nOut of chips!\nGame over!"
