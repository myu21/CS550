"""
Mitchell Yu
Fall Final Project
12 November 2018
I chose the maze prompt for my final project. I didn't really use the full Prims Algorithm and create a weighted grid, rather I just allowed the head of each path to move in a random direction. Since the weighted grid would have been randomized anyways, the effect would be the same. In this program, any coordinate that still has the possibility of "moving" in any direction would do so until it reached a dead end. Then I changed it from a leading coordinate to just a visited one.
I faced a lot of challenges in the beginning because I kept on thinking that I would have to either use classes or recursive functions for the paths to randomly stretch across the screen. These solutions may have worked, though I hit a wall and for a while my code could only generate a singular path (which would make solving the maze way too easy)
I think taking the more basic approach eliminated any possible areas for error, and the code seems to work out quite well.
I had some time, so I decided that I wanted to transfer the maze into a image instead of simply printing on the screen. I made it so each coordinate would represent a box of pixels, and then from there I could just fill the pixels up when needed.
I recomend going over a 50x50 maze, because that's when it really starts looking good (also the 10x10 mazes are really easy to solve) The code also works pretty well for non-square mazes (except for when the width or height is one unit, which would be a really boring maze anyways)
On My Honor: Mitchell Yu
"""

import random as r
from PIL import Image
print("Welcome to the maze generator!")
while True:
	try:
		width = int(input("What would you like the width of the maze to be?\n>> "))
		height = int(input("What would you like the height of the maze to be?\n>> "))
		celldim = int(input("What would you like the pixel dimensions of each box to be?\n>> "))
		break
	except ValueError:
		print("Sorry, please input integers.")
print("Thank you for using the maze generator, your maze will be done shortly!")
imgx = width*celldim
imgy = height*celldim
image = Image.new("RGB", (imgx, imgy))

board = [[0]*(width+2) for x in range(height+2)] # creates grid for board (I wanted to add margins to prevent any possibility of the code using the wrong array coordinates during the conversions)

orient = r.randint(0,1) # decides whether the solution moves along the width or length
startx = r.randint(1,width)
starty = r.randint(1,height)
if orient == 0:
	board[1][startx] = 2
else:
	board[starty][1] = 2

for z in range(width*height): # so it checks over every coordinate once
	for x in range(1, width):
		for y in range(1, height):
			if board[y][x] == 2: # when a board coordinate is equal to 2, it means that that coordinate is the leading path for the maze
				deadend = [0,0,0,0] # a set that keeps a check of whether all four directions are blocked (hence the name deadend)
				while True:
					if deadend[0] + deadend[1] + deadend[2] + deadend[3] <=3:
						change = r.randint(0,3) # randomly chooses which direction to move in
						if change == 0:
							if board[y-1][x] < 1 and board[y-1][x-1] < 1 and board[y-1][x+1] < 1 and board[y-2][x] < 1 and y > 1: # makes sure that the coordinate the maze path is moving into is not touching with another path, is not already a path, and is not colliding into a wall
								board[y-1][x] = 2 # sets the new path head as the leading coordinate
								break
							else:
								deadend[0] = 1 # checks this coordinate off as a deadend
						elif change == 1:
							if board[y+1][x] < 1 and board[y+1][x-1] < 1 and board[y+1][x+1] < 1 and board[y+2][x] < 1 and y < height:
								board[y+1][x] = 2
								break
							else:
								deadend[1] = 1
						elif change == 2:
							if board[y][x+1] < 1 and board[y-1][x+1] < 1 and board[y+1][x+1] < 1 and board[y][x+2] < 1 and x < width:
								board[y][x+1] = 2
								break
							else:
								deadend[2] = 1
						else:
							if board[y][x-1] < 1 and board[y-1][x-1] < 1 and board[y+1][x-1] < 1 and board[y][x-2] < 1 and x > 1:
								board[y][x-1] = 2
								break
							else:
								deadend[3] = 1
					else:
						board[y][x] = 1 # once this path head has no possible place to go (no further branches can be made), it is set as a visited coordinate
						break

for x in range(1, width+1):
	for y in range(1, height+1):
		if board[y][x] >= 1:
			for xx in range(celldim):
				for yy in range(celldim):
					image.putpixel(((celldim*(x-1))+xx,(celldim*(y-1))+yy),(255,255,255)) # just putting white pixels within each coordinate square

if orient == 0: # coloring in starting and ending blocks for the maze
	while True:
		endx = r.randint(1,width)
		if board[height][endx] == 2:
			for xx in range(celldim):
				for yy in range(celldim):
					image.putpixel((celldim*(startx-1)+xx,yy),(0,255,0))
					image.putpixel((celldim*(endx-1)+xx,celldim*(height-1)+yy),(255,0,0))
			break
else:
	while True:
		endy = r.randint(1,height)
		if board[endy][width] == 2:
			for xx in range(celldim):
				for yy in range(celldim):
					image.putpixel((xx,celldim*(starty-1)+yy),(0,255,0))
					image.putpixel((celldim*(width-1)+xx,celldim*(endy-1)+yy),(255,0,0))
			break

image.save("maze.png","PNG")