import random

class card:
	def __init__(self, value, suite):
		self.value = value
		self.suite = suite

x = card(random.randint(2,14), random.randint(1,4))

print(x.value, x.suite)