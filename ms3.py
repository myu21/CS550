"""
Mitchell Yu
Mindfield Project
I think after the board setup, the whole project was pretty smooth sailing from there. In this version of Mindfield, you will be able to uncover flags you previously planted, as well replay the game after you finish. I also made it so the board will apear in the same spot at the bottom of the screen after every turn to make the game less confusing. I did however have a little trouble developing the "clicking on zero and uncovering all the zeros". After looking at the many solutions online, they all look insanely complicated for my level of coding, so I decided just to let that go. I guess it'll just be a really hard game of Mindfield.
Citations:
Control the # of digits of a diplayed integer - Ms. Healy
On my honor - Mitchell Yu
"""
import random
import sys

width = int(sys.argv[1])
height = int(sys.argv[2])
bomb = int(sys.argv[3])
bh = height + 2
bw = width + 2
digits = 0

#Making sure the spacing isn't all wonky (it adjusts for any dimension of the board)
if width>height:
	xtemp = width
else:
	xtemp = height
while xtemp >= 1:
	xtemp = xtemp/10
	digits += 1

def start():
	#Board setup
	global displayboard
	global trueboard
	trueboard = [[0]*(bw) for x in range(bh)]
	try:
		for z in range(bomb):
			while True:
				x = random.randint(1, bw-2)
				y = random.randint(1, bh-2)
				if trueboard[y][x] != "*":
					trueboard[y][x] = "*"
					break
			if trueboard[y-1][x-1] != "*":
				trueboard[y-1][x-1] += 1
			if trueboard[y+1][x-1] != "*":
				trueboard[y+1][x-1] += 1
			if trueboard[y+1][x+1] != "*":
				trueboard[y+1][x+1] += 1
			if trueboard[y-1][x+1] != "*":
				trueboard[y-1][x+1] += 1
			if trueboard[y-1][x] != "*":
				trueboard[y-1][x] += 1
			if trueboard[y][x-1] != "*":
				trueboard[y][x-1] += 1
			if trueboard[y][x+1] != "*":
				trueboard[y][x+1] += 1
			if trueboard[y+1][x] != "*":
				trueboard[y+1][x] += 1
	except IndexError:
		pass
	#Display board setup
	displayboard = [[(digits-1)*" "+"□"]*(width+1) for x in range(height+1)]
	for x in range(width+1):
		displayboard[0][x] = str(x).zfill(digits)
	for x in range(height+1):
		displayboard[x][0] = str(x).zfill(digits)
	for x in range(40):
		print(" ")
	userturn()

def userturn():
	wintest()
	try:
		global xcheck
		global ycheck
		display()
		movetype = int(input("Would you like to place a flag(1), unpick a flag(2) or uncover a square(3)?\n>>"))
		for x in range(40):
			print(" ")
		display()
		ycord = int(input("Which row would you like to choose?\n>>"))
		for x in range(40):
			print(" ")
		display() #The repeating of the display function may seem like dry coding, but my intent was for the board to remain in the same position every turn. It looked really confusing when the board kept on jumping up and down, so this ensures that the board is always displayed right above the question prompt.
		xcord = int(input("Which column would you like to choose?\n>>"))
		for x in range(40):
			print(" ")
		if movetype>= 1 and movetype<=3:
			if (xcord>=1 and xcord<=width) and (ycord>=1 and ycord<=height):
				if movetype == 1:
					if displayboard[ycord][xcord] == (digits-1)*" "+"□":
						displayboard[ycord][xcord] = (digits-1)*" "+"P"
						userturn()
					elif displayboard[ycord][xcord] == (digits-1)*" "+"P":
						print("There is already a flag in this position")
						userturn()
					else:
						print("This space is already uncovered")
						userturn()
				elif movetype == 2:
					if displayboard[ycord][xcord] == (digits-1)*" "+"P":
						displayboard[ycord][xcord] = (digits-1)*" "+"□"
						userturn()
					else:
						print("There is no flag in this position.")
						userturn()
				elif movetype == 3:
					if displayboard[ycord][xcord] == (digits-1)*" "+"P" or displayboard[ycord][xcord] == (digits-1)*" "+"□":
						xcheck = xcord
						ycheck = ycord
						checksquare()
					else:
						print("This space is already uncovered")
						userturn()
			else:
				print("Please input a coordinate value that is on the board")
				userturn()
		else:
			print("That is not a valid move")
			userturn()
	except ValueError:
		print("That is not a valid input")
		userturn()

def checksquare():
	if trueboard[ycheck][xcheck] == "*":
		print("Sorry, you lost.")
		end()
	else:
		displayboard[ycheck][xcheck] = (digits-1)*" "+str(trueboard[ycheck][xcheck])
		userturn()

def display():
	for x in range(len(displayboard)):
		print(*displayboard[x])

def wintest():
	winct = 0
	for x in range(1,width+1):
		for y in range(1,height+1):
			if displayboard[y][x] == (digits-1)*" "+"P" and trueboard[y][x] == "*":
				winct += 1
	if winct >= bomb:
		print("You won!")
		end()

def end():
	for x in range(1,width+1):
		for y in range(1,height+1):
			displayboard[y][x] = (digits-1)*" "+str(trueboard[y][x])
	for x in range(len(displayboard)):
		print(*displayboard[x])
	end = input("Would you like to play again (y/n)\n>>")
	if end == "y":
		start()
	elif end == "n":
		print("Thanks for playing!")
		sys.exit()
	else:
		print("I'll take that as a no. Thanks for playing!")
		sys.exit()

start()