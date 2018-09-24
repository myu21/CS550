"""
Mitchell YU
9/24/2018
Text-Game - Black Jack
I tried to create a very stripped down version of Black Jack. I didn't include any sort of spliting or anything fancy, just the basic rules. You may see a few places where I violated the DRY coding policy, but I decided that it was more important for the game to be completely bug free. I think the main challenge was deciding how to model the cards in the program efficiently, and it was pretty smooth sailing after that decision. There are certain places where I know loops would be much more efficient, but I didn't want to run before I could walk. (BIG HINT: if you want to break my game, then try to hit more than five times. I didn't allow for the full 9 possible hits because there is such a small chance of actually needing that many cards)
For the most part, I'm pretty happy with the outcome. The game can be replayed, and it also keeps track of the money. I actually decided to give the dealer a slight edge, as it has a smaller chance of busting.
I learned how to use classes from: https://docs.python.org/3/tutorial/classes.html
On my honor - Mitchell Yu
"""
import random
class card:
	def __init__(self, value, suite):
		self.value = value
		self.suite = suite
cash = 100
print("Hello there!")
def start():
	global cash
	play = input("You currently have $"+str(cash)+". Would you like to play? (y/n)\n>>")
	if play == "y":
		playerbet();
	elif play == "n":
		print("Thank you for playing.")
		exit()
	else:
		print("Please type either 'y' or 'n'")
		start()

def playerbet():
	global bet
	while True:
		try:
			bet = float(input("How much would you like to bet?\n>>"))
			if bet > float(cash):
				print("You don't have enough money.")
			elif bet>0:
				print("Good luck!")
				draw()
				break
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
	global dealer
	suites = ("Hearts", "Clubs", "Diamonds", "Spades")
	draw1 = card(random.randint(2,14), random.choice(suites))
	draw2 = card(random.randint(2,14), random.choice(suites))
	drawnum = 0
	while True:
		if draw1.value == draw2.value and draw1.suite == draw2.value:
			draw2 = card(random.randint(2,14), random.choice(suites))
		else:
			break
	dealer = random.randint(17,24)
	if dealer >= 22:
		dealer = random.randint(17,24)
	print("The dealer has a score of:", dealer)
	display(draw1.value, draw1.suite)
	display(draw2.value, draw2.suite)
	while True: 
		response = input("Would you like to hit or stand?\n>>")
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
			if (draw3.value == draw1.value and draw3.suite == draw1.suite) or (draw3.value == draw3.value and draw2.suite == draw2.suite):
				draw3 = card(random.randint(2,14), random.choice(suites))
				break
		drawnum = 1
		display(draw3.value, draw3.suite)
		hit2()
def hit2():
	global draw4
	global drawnum
	while True: 
		response = input("Would you like to hit or stand?\n>>")
		if response == "hit":
			draw4 = card(random.randint(4,14), random.choice(suites))
			while True:
				if (draw4.value == draw1.value and draw4.suite == draw1.suite) or (draw4.value == draw2.value and draw4.suite == draw2.suite) or (draw4.value == draw3.value and draw4.suite == draw3.suite):
					draw4 = card(random.randint(2,14), random.choice(suites))
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
		response = input("Would you like to hit or stand?\n>>")
		if response == "hit":
			draw5 = card(random.randint(6,14), random.choice(suites))
			while True:
				if (draw5.value == draw1.value and draw5.suite == draw1.suite) or (draw5.value == draw2.value and draw5.suite == draw2.suite) or (draw5.value == draw3.value and draw5.suite == draw3.suite) or (draw5.value == draw4.value and draw5.suite == draw4.suite):
					draw5 = card(random.randint(2,14), random.choice(suites))
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
	global draw1, draw2, draw3, draw4, draw5
	global cash
	if draw1.value >= 14:
		draw1.value = 11
	elif draw1.value >= 11:
		draw1.value = 10
	if draw2.value >= 14:
		draw2.value = 11
	elif draw2.value >= 11:
		draw2.value = 10
	if drawnum == 3:
		if draw5.value >= 14:
			draw5.value = 11
		elif draw5.value >+ 11:
			draw5.value = 10
		playertotal = draw5.value+draw4.value+draw3.value+draw2.value+draw1.value
	elif drawnum == 2:
		if draw4.value >= 14:
			draw4.value = 11
		elif draw4.value >= 11:
			draw4.value = 10	
		playertotal = draw4.value+draw3.value+draw2.value+draw1.value
	elif drawnum == 1:
		if draw3.value >= 14:
			draw3.value = 11
		elif draw3.value >= 11:
			draw3.value = 10
		playertotal = draw3.value+draw2.value+draw1.value
	else:
		playertotal = draw2.value+draw1.value
	if playertotal >= 22:
		print("That's a bust, you lose.")
		cash = float(cash) - float(bet)
	elif dealer >= 22:
		print("Dealer busts, you win!")
		cash = float(cash) + float(bet)
	elif playertotal > dealer:
		print("You win!")
		cash = float(cash) + float(bet)
	elif playertotal == dealer:
		print("It's a tie.")
	else:
		print("Dealer wins, you lose.")
		cash = float(cash) - float(bet)
	if float(cash) <= 0:
		print("Sorry, you are all out of money. Thank you for playing.")
		exit()
	start()

start()