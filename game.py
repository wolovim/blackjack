from deck import Deck
from hand import Hand

class Game:
  def __init__(self):
    self.chips = 100

  def play(self):
    print "\nA crappy blackjack game appears!"
    while self.is_live():
      deck = Deck()
      player_hand = self.deal_hand(deck)
      dealer_hand = self.deal_hand(deck)
      bet = self.get_player_bet()
      self.display_hands(player_hand, dealer_hand)
      self.handle_user_actions(deck, bet, player_hand, dealer_hand)
    else:
      print "\nOut of chips!\nGame over!"

  def is_live(self):
    return self.chips > 0

  def deal_hand(self, deck):
    hand = Hand()
    deck.deal(hand)
    return hand

  def display_hands(self, player_hand, dealer_hand):
    print "\nYour hand: {hand}".format(hand=self.display_player_hand(player_hand.cards))
    print "Dealer's hand: {hand}\n".format(hand=self.display_dealer_hand(dealer_hand.cards))

  def display_player_hand(self, hand):
    return "{card_1}, {card_2}".format(card_1=hand[0], card_2=hand[1])

  def display_dealer_hand(self, hand):
    return "{card_1}, HIDDEN".format(card_1=hand[0])

  def get_player_bet(self):
    while True:
      try:
        print "\nYou have {chips} chips.".format(chips=self.chips)
        bet = int(raw_input("How many would you like to bet? "))
        if bet > self.chips:
          print "You can't bet more than you have!"
          continue
        elif bet < 1:
          print "Bet must be at least 1!"
          continue
        else:
          return bet
      except:
        print "\nPlease enter a number of chips!"

  def handle_user_actions(self, deck, bet, player_hand, dealer_hand):
    while True:
      input = raw_input('Want to (h)it or (s)tay? ')

      if input == 'h':
        print 'Hitting!'
        deck.hit(player_hand)
        if self.is_bust(player_hand):
          print 'Bust!'
          self.lose_chips(bet)
          break
      elif input == 's':
        self.evaluate_round(bet, player_hand, dealer_hand)
        break
      else:
        print "\nGotta enter 'h' or 's'!"
        continue

  def is_bust(self, hand):
    return hand.get_value() > 21

  def evaluate_round(self, bet, player_hand, dealer_hand):
    player_points = player_hand.get_value()
    dealer_points = dealer_hand.get_value()
    print "Your total: {player}. Dealer's total: {dealer}".format(player=player_points,dealer=dealer_points)
    if player_points > dealer_points:
      print 'You win!'
      self.win_chips(bet)
    elif player_points == dealer_points:
      print 'Push!'
    else:
      print 'You lose!'
      self.lose_chips(bet)

  def win_chips(self, chips):
    self.chips += chips

  def lose_chips(self, chips):
    self.chips -= chips
