values = { 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

class Game:
  def __init__(self):
    self.chips = 100

  def evaluate_hand(self, hand):
    value = 0
    for card in hand:
      value += values[card[1:]]
    return value

  def evaluate_round(self, bet, player_hand, dealer_hand):
    player_points = self.evaluate_hand(player_hand)
    dealer_points = self.evaluate_hand(dealer_hand)
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
