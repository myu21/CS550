import random

class account:

	def __init__(self, username, pin):
		self.username = username
		self.balance = 0
		self.pin = int(pin)
		self.accountnum = random.randint(0,9999999999999999)
		self.openclose = 1

	def deposit(self, value):
		self.balance += value
		status = "You have deposited "+value+" dollars into your account"
		return status

	def withdraw(self, value):
		if value<self.balance:
			self.balence -= value
			status = "You have withdrawn "+value+" dollars from your account"
		else:
			status = "Sorry, you cannot withdraw a value greater than your balance"
		return status

	def stats(self):
		info = "Name: "+ self.username
		info += "\nAccount Number: "+ self.accountnum
		info += "\nBalance: "+ self.balance
		return info
#"%04d" % 
def createaccount():
	username = input("What is your name?")
	while True:
		pin = %04d input("What would you like your pin to be? (please input 4 digit code)")
		if pin >= 0 and pin < 10000:
			break
	account1 = account(username, pin)
	print("Congrats! You successfully created an account")

def accountlogin():
	username = input 

def userturn():
	turntype = input("What would you like to do?\nLogin to account (1)\nCreate account (2)\nQuit (3)")
	if turntype == "2":
		createaccount()
	elif turntype == "1":
		accountlogin()
	elif turntype == "3":
		quit()
	else:
		print("Please type a valid input (1, 2, or 3)")