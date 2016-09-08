values = { 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

class Game:
  def __init__(self):
    self.chips = 100
    self.hand = []

  def evaluate_hand(self, hand):
    value = 0
    for card in hand:
      value += values[card[1:]]
    return value

  def evaluate_round(self, player_hand, dealer_hand):
    return 'win!' if self.evaluate_hand(player_hand) > self.evaluate_hand(dealer_hand) else 'lose!'

  def win_chips(self, chips):
    self.chips += chips

  def lose_chips(self, chips):
    self.chips -= chips
