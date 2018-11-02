import random as r
width = 50#int(sys.argv[1])
height = 50#int(sys.argv[2])

board = [[0]*(width) for x in range(height)]

board[r.randint(height)][0] = 1

for x in range(width):
	for y in range(height):
		if board[y][x] == 1 and (board[y-1][x]+board[y+1][x]+board[y][x-1]+board[y][x+] == 1):
			while True:
				choose = r.randint(3)
				if choose == 0:	
					board[x]
				elif choose == 1:

				elif choose == 2:

				elif choose == 3: