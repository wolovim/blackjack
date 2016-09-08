from random import shuffle

class Deck:
  def __init__(self, suits, ranks):
    deck = [suit + rank for suit in suits for rank in ranks]
    shuffle(deck)
    self.deck = deck

  def deal(self):
    hand = []
    hand.append(self.deck.pop())
    hand.append(self.deck.pop())
    return hand

