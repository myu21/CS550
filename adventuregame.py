import random

class card:
	def __init__(self, value, suite):
		self.value = value
		self.suite = suite

cash = 100

def start():
	global play
	play = input("Hello there, you currently have $"+str(cash)+". Would you like to play? (y/n)")
	if play == "y":
		bet();
	elif play == "n":
		print("Thank you for playing.")
	else:
		print("Please type either 'y' or 'n'")
		start()

def bet():
	global bet
	while True:
		try:
			bet = int(input("How much would you like to bet?"))
			if bet <= cash and bet>0:
				print("Good luck!")
				draw()
				break
			elif bet > cash:
				print("You don't have enough money.")
			else:
				print("Nice try.")
		except ValueError:
			print("That's not a number, try again")

class display:
	def __init__(self, value, suite):
		if value <= 10 and value >= 2:
			print(str(value)+" of "+suite)
		elif value == 11:
			print("J of "+suite)
		elif value == 12:
			print("Q of "+suite)
		elif value == 13:
			print("K of "+suite)
		else:
			print("A of "+suite)

def draw():
	global suites
	global drawnum
	global draw1
	global draw2
	suites = ("Hearts", "CLubs", "Diamonds", "Spades")
	draw1 = card(random.randint(2,14), random.choice(suites))
	draw2 = card(random.randint(2,14), random.choice(suites))
	drawnum = 0
	while True:
		if draw1.value == draw2.value and draw1.suite == draw2.value:
			draw2 = card(random.randint(2,14), random.randint(1,4))
		else:
			break
	dealer = random.randint(17,24)
	print("The dealer has a score of:", dealer)
	display(draw1.value, draw1.suite)
	display(draw2.value, draw2.suite)
	while True: 
		response = input("Would you like to hit or stand?")
		if response == "hit":
			hit1()
			break
		elif response == "stand":
			result()
			break
		else:
			print("Please enter either 'hit' or 'stand'")

def hit1():
	global draw3
	global drawnum
	while True: 
		draw3 = card(random.randint(2,14), random.choice(suites))
		while True:
			if (draw3.value == draw1.value and draw3.suite == draw1.value) or (draw3.value == draw3.value and draw2.suite == draw2.value):
				draw3 = card(random.randint(2,14), random.randint(1,4))
			else:
				break
		drawnum = 1
		display(draw3.value, draw3.suite)
		hit2()
def hit2():
	global draw4
	global drawnum
	while True: 
		response = input("Would you like to hit or stand?")
		if response == "hit":
			draw4 = card(random.randint(4,14), random.choice(suites))
			while True:
				if (draw4.value == draw1.value and draw4.suite == draw1.value) or (draw4.value == draw2.value and draw4.suite == draw2.value) or (draw4.value == draw3.value and draw4.suite == draw3.value):
					draw4 = card(random.randint(2,14), random.randint(1,4))
				else:
					break
			drawnum = 2
			display(draw4.value, draw4.suite)
			hit3()
		elif response == "stand":
			result()
			break
		else:
			print("Please enter either 'hit' or 'stand'")

def hit3():
	global draw5
	global drawnum
	while True: 
		response = input("Would you like to hit or stand?")
		if response == "hit":
			draw5 = card(random.randint(6,14), random.choice(suites))
			while True:
				if (draw5.value == draw1.value and draw5.suite == draw1.value) or (draw5.value == draw2.value and draw5.suite == draw2.value) or (draw5.value == draw3.value and draw5.suite == draw3.value) or (draw5.value == draw4.value and draw5.suite == draw4.value):
					draw5 = card(random.randint(2,14), random.randint(1,4))
				else:
					break
			drawnum = 3
			display(draw5.value, draw5.suite)
			result()
			break
		elif response == "stand":
			result()
			break
		else:
			print("Please enter either 'hit' or 'stand'")

def result():
	print("hi")


start()