from random import shuffle

suits = ['C', 'H', 'S', 'D']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
  def __init__(self):
    deck = [suit + rank for suit in suits for rank in ranks]
    shuffle(deck)
    self.deck = deck

  def deal(self, hand):
    hand.cards.append(self.deck.pop())
    hand.cards.append(self.deck.pop())

  def hit(self, hand):
    hand.cards.append(self.deck.pop())
    print "Current hand: {cards}\n".format(cards=hand.cards)
