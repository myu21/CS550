"""
Working MindField
"""

import random
import sys

width = int(sys.argv[1])
height = int(sys.argv[2])
bomb = int(sys.argv[3])
bh = height + 2
bw = width + 2
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

displayboard = [["□"]*(width+1) for x in range(height+1)]
for x in range(width+1):
	displayboard[0][x] = x
for x in range(height+1):
	displayboard[x][0] = x

def userturn():
	for x in range(len(displayboard)):
		print(*displayboard[x])
	global xcheck
	global ycheck
	movetype = int(input("Would you like to place a flag(1), unpick a flag(2) or uncover a square(3)?"))
	ycord = int(input("Which row would you like to choose?"))
	xcord = int(input("Which column would you like to choose?"))
	if (xcord<1 or xcord>width) and (ycord<1 or ycord>height):
		print("Please input a coordinate value that is on the board")
		userturn()
	else:
		if movetype == 1:
			if displayboard[ycord][xcord] == "□":
				displayboard[ycord][xcord] = "P"
				userturn()
			elif displayboard[ycord][xcord] == "P":
				print("There is already a flag in this position")
				userturn()
			else:
				print("This space is already uncovered")
				userturn()
		elif movetype == 2:
			if displayboard[ycord][xcord] == "P":
				displayboard[ycord][xcord] = "□"
				userturn()
			else:
				print("There is no flag in this position.")
				userturn()
		elif movetype == 3:
			if displayboard[ycord][xcord] == "P" or displayboard[ycord][xcord] == "□":
				xcheck = xcord
				ycheck = ycord
				checksquare()
			else:
				print("This space is already uncovered")
				userturn()

def checksquare():
	if trueboard[ycheck][xcheck] == "*":
		lose()
	else:
		displayboard[ycheck][xcheck] = trueboard[ycheck][xcheck]
		userturn()

def lose():
	print("Sorry you lose.")
	for x in range(1,width+1):
		for y in range(1,height+1):
			displayboard[y][x] = trueboard[y][x]
	for x in range(len(displayboard)):
		print(*displayboard[x])

userturn()