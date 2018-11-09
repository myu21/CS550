from PIL import Image
import random as r
width = 20
height = 20

board = [[0]*(width) for x in range(height)]

board[10][10] = 1


def boardcheck(x,y):
	if x <= 0 or x >= width or y <= 0 or y >= height:
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
						return "working"
					else:
						deadend[0] = 1
				elif change == 1:
					if board[y+1][x] != 1 and board[y+1][x-1] != 1 and board[y+1][x+1] !=1 and board[y+2][x] != 1:
						board[y+1][x] = 1
						boardcheck(x,y+1)
						return "working"
					else:
						deadend[1] = 1
				elif change == 2:
					if board[y][x+1] != 1 and board[y-1][x+1] != 1 and board[y+1][x+1] !=1 and board[y][x+2] != 1:
						board[y][x+1] = 1
						boardcheck(x+1,y)
						return "working"
					else:
						deadend[2] = 1
				else:
					if board[y][x-1] != 1 and board[y-1][x-1] != 1 and board[y+1][x-1] !=1 and board[y][x-2] != 1:
						board[y][x-1] = 1
						boardcheck(x-1,y)
						return "working"
					else:
						deadend[3] = 1
			else:
				return "working"
	except IndexError:
		pass

for z in range(1000):
	for x in range (1,width-1):
		for y in range (1,height-1):
			if board[y][x] == 1:
				boardcheck(x,y)


for x in range(len(board)):
		print(*board[x])

