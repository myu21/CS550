import random as r
width = 10
height = 10

board = [[0]*(width+2) for x in range(height+2)]

board[1][1] = 2

for z in range (width*height):
	for x in range(1, width):
		for y in range(1, height):
			if board[y][x] == 2:
				deadend = [0,0,0,0]
				while True:
					if deadend[0] + deadend[1] + deadend[2] + deadend[3] <=3:
						change = r.randint(0,3)
						if change == 0:
							if board[y-1][x] < 1 and board[y-1][x-1] < 1 and board[y-1][x+1] < 1 and board[y-2][x] < 1 and y > 1:
								board[y-1][x] = 2
								break
							else:
								deadend[0] = 1
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
						board[y][x] = 1
						break


for x in range(len(board)):
		print(*board[x])
