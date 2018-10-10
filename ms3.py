"""
Mitchell Yu
Mindfield Project

I think after the board setup, the whole project was pretty smooth sailing from there. In this version of Mindfield, you will be able to uncover flags you previously planted, as well replay the game after you finish. I also made it so the board will apear in the same spot at the bottom of the screen after every turn to make the game less confusing.

I did however have a little trouble developing the "clicking on zero and uncovering all the zeros". After looking at the many solutions online, they all look insanely complicated for my level of coding, so I decided just to let that go.
[EDIT (Oct 8th): I had a revelation today just after class, and I understood EXACTLY what I was missing. So I decided to solve it to give me the satisfaction of successfully creating minefield. I didn't even need recursions, I simply checked each display value for a zero, and if it was a zero, it would uncover everything around it. I put this in a for loop in order to fully catch all of the possible zeros (assuming you play it in a reasonable sized board ie not 1000x1000). I'm personally really pleased with this solution (even though its not exactly the most efficient solution I have come up with). Feel free to grade it as a late assignment]

Citations:
Control the # of digits of a diplayed integer - Ms. Healey
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

def firstturn():
	global displayboard
	global fycord
	global fxcord
	displayboard = [[(digits-1)*" "+"□"]*(width+1) for x in range(height+1)]
	for x in range(width+1):
		displayboard[0][x] = str(x).zfill(digits)
	for x in range(height+1):
		displayboard[x][0] = str(x).zfill(digits)
	try:
		display()
		fycord = int(input("Which row would you like to choose?\n>>"))
		display()
		fxcord = int(input("Which column would you like to choose?\n>>"))
		if (fxcord>=1 and fxcord<=width) and (fycord>=1 and fycord<=height):
			start()
			displayboard[fycord][fxcord] = (digits-1)*" "+str(trueboard[fycord][fxcord])
			fillzero()
			userturn()
		else:
			print("Please input a coordinate value that is on the board")
			firstturn()
	except ValueError:
		print("That is not a valid input")
		firstturn()

def fillzero():
	#Uncovers the zeros
	global displayboard
	for z in range(5):
		try:
			for x in range(1,width):
				for y in range(1,height):
					if displayboard[y][x] == (digits-1)*" "+"0":
						displayboard[y][x+1] = (digits-1)*" "+str(trueboard[y][x+1])
						displayboard[y][x-1] = (digits-1)*" "+str(trueboard[y][x-1])
						displayboard[y+1][x+1] = (digits-1)*" "+str(trueboard[y+1][x+1])
						displayboard[y+1][x-1] = (digits-1)*" "+str(trueboard[y+1][x-1])
						displayboard[y+1][x] = (digits-1)*" "+str(trueboard[y+1][x])
						displayboard[y-1][x] = (digits-1)*" "+str(trueboard[y-1][x])
						displayboard[y+1][x-1] = (digits-1)*" "+str(trueboard[y+1][x-1])
						displayboard[y-1][x-1] = (digits-1)*" "+str(trueboard[y-1][x-1])
		except IndexError:
			pass

def start():
	#Board setup
	global trueboard
	trueboard = [[0]*(bw) for x in range(bh)]
	try:
		for z in range(bomb):
			while True:
				x = random.randint(1, bw-2)
				y = random.randint(1, bh-2)
				if (trueboard[y][x] != "*") and (x != fxcord and y+1 != fycord) and (x != fxcord and y-1 != fycord) and (x+1 != fxcord and y != fycord) and (x-1 != fxcord and y != fycord) and (x+1 != fxcord and y+1 != fycord) and (x+1 != fxcord and y-1 != fycord) and (x-1 != fxcord and y+1 != fycord) and (x-1 != fxcord and y-1 != fycord):
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

def userturn():
	wintest()
	try:
		global xcheck
		global ycheck
		display()
		movetype = int(input("Would you like to place a flag(1), unpick a flag(2) or uncover a square(3)?\n>>"))
		display()
		ycord = int(input("Which row would you like to choose?\n>>"))
		display() #The repeating of the display function may seem like dry coding, but my intent was for the board to remain in the same position every turn. It looked really confusing when the board kept on jumping up and down, so this ensures that the board is always displayed right above the question prompt.
		xcord = int(input("Which column would you like to choose?\n>>"))
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
		firstturn()
	elif end == "n":
		print("Thanks for playing!")
		sys.exit()
	else:
		print("I'll take that as a no. Thanks for playing!")
		sys.exit()

firstturn()