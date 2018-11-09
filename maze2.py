from PIL import Image
import random as r
width = 20
height = 20

board = [[0]*(width) for x in range(height)]

board[7][7] = 1
board[13][13]=1


def boardcheck(x,y):
	if x <= 0 or x >= width-1 or y <= 0 or y >= height-1:
		return "working"
	deadend = [0,0,0,0]
	try:
		while True:
			if deadend[0] + deadend[1] + deadend[2] + deadend[3] <=3:
				change = r.randint(0,3)
				if change == 0:
					if board[y-1][x] != 1 and board[y-1][x-1] != 1 and board[y-1][x+1] !=1 and board[y-2][x] != 1:
						board[y-1][x] = 1
						boardcheck(x,y-1)
						break
					else:
						deadend[0] = 1
						break
				elif change == 1:
					if board[y+1][x] != 1 and board[y+1][x-1] != 1 and board[y+1][x+1] !=1 and board[y+2][x] != 1:
						board[y+1][x] = 1
						boardcheck(x,y+1)
						break
					else:
						deadend[1] = 1
						break
				elif change == 2:
					if board[y][x+1] != 1 and board[y-1][x+1] != 1 and board[y+1][x+1] !=1 and board[y][x+2] != 1:
						board[y][x+1] = 1
						boardcheck(x+1,y)
						break
					else:
						deadend[2] = 1
						break
				else:
					if board[y][x-1] != 1 and board[y-1][x-1] != 1 and board[y+1][x-1] !=1 and board[y][x-2] != 1:
						board[y][x-1] = 1
						boardcheck(x-1,y)
						break
					else:
						deadend[3] = 1
						break
			else:
				break
	except IndexError:
		pass

for z in range(100000):
	for x in range (1,width-1):
		for y in range (1,height-1):
			if board[y][x] == 1 and board[y-1][x]+board[y+1][x]+board[y][x-1]+board[y][x+1] <=1:
				boardcheck(x,y)
for z in range(100000):
	for x in range (1,width-1):
		for y in range (1,height-1):
			if board[y][x] == 1 and board[y-1][x]+board[y+1][x]+board[y][x-1]+board[y][x+1] <=1:
				boardcheck(x,y)

for x in range(len(board)):
		print(*board[x])

