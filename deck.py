import sys
from card import Card
class Deck:

	def __init__(self, handtype):
		self.handtype = handtype
		self.deck = []
		if self.handtype != "hand":
			for x in range(1,14):
				cardtemp1 = Card("Diamonds",x)
				cardtemp2 = Card("Clubs",x)
				cardtemp3 = Card("Hearts",x)
				cardtemp4 = Card("Spades",x)
				self.deck.append(cardtemp1.display())
				self.deck.append(cardtemp2.display())
				self.deck.append(cardtemp3.display())
				self.deck.append(cardtemp4.display())
	def display(self):
		return self.deck
deck1 = Deck("not hand")
print(*deck1.display())