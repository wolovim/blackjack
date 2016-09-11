values = { 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

class Hand:
  def __init__(self):
    self.cards = []
    self.ace = False

  def deal(self, deck):
    self.cards.append(deck.cards.pop())
    self.cards.append(deck.cards.pop())
    self.check_for_ace()

  def hit(self, deck):
    self.cards.append(deck.cards.pop())
    self.check_for_ace()
    print "Current hand: {cards}\n".format(cards=self.cards)

  def get_value(self):
    value = 0
    for card in self.cards:
      value += values[card[1:]]
    if self.ace and value < 12:
      value += 10
    return value

  def check_for_ace(self):
    for card in self.cards:
      if card[1:] == 'A':
        self.ace = True
