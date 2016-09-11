values = { 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

class Hand:
  def __init__(self):
    self.cards = []

  def get_value(self):
    value = 0
    for card in self.cards:
      value += values[card[1:]]
    return value
