class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def display(self):
		if self.rank == 1:
			show = "Ace of "+self.suit
		elif self.rank == 11:
			show = "Jack of "+self.suit
		elif self.rank == 12:
			show = "Queen of "+self.suit
		elif self.rank == 13:
			show = "King of "+self.suit
		else:
			show = str(self.rank)+" of "+self.suit
		return show + "\n"