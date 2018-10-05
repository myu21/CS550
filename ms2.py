import random
import sys

width = int(sys.argv[1])
height = int(sys.argv[2])
bomb = int(sys.argv[3])
board = []

board = [[0]*(width) for x in range(height)]

for x in range(bomb):
	try:
		h = random.randint(0, height-1)
		l = random.randint(0, width-1)
		board[h][l] = "*"
		if l!=0:
			if h!=0:
				board[h-1][l-1] += 1
			board[h+1][l-1] += 1
			board[h][l-1] += 1
		if h!=0:
			board[h-1][l+1] += 1
			board[h-1][l] += 1
			print("indicate1")
		board[h][l+1] += 1
		print("indicate 2")
		board[h+1][l] += 1
		board[h+1][l+1] += 1
	except IndexError:
		pass
	except ValueError:
		pass

for x in range(len(board)):
	print(*board[x])