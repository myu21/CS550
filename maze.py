from PIL import Image
import random as r
width = 25#int(sys.argv[1])
height = 25#int(sys.argv[2])

image = Image.new("RGB", (width, height))

board = [[0]*(width) for x in range(height)]

def boardcheck(x,y):
	while True:
		if x >= 1 and x <= width-1 and y >= 1 and y <= height-1:
			choose = r.randint(0,3)
			if choose == 0:
				if board[y-1][x] == 0:
					board[y-1][x] = 1
					boardcheck(y-1,x)
					break
			elif choose == 1:
				if board[y+1][x] ==0:
					board[y+1][x] = 1
					boardcheck(y+1,x)
					break
			elif choose == 2:
				if board[y][x-1] ==0:
					board[y][x-1] = 1
					boardcheck(y,x-1)
					break
			elif choose == 3:
				if board[y][x+1] ==0:
					board[y][x+1] = 1
					boardcheck(y,x+1)
					break		
		else:
			break	

board[1][2] = 1
board[1][1] = 1
for x in range(width-1):
	for y in range(height-1):
		if board[y][x] == 1 and (board[y-1][x]+board[y+1][x]+board[y][x-1]+board[y][x+1] == 1):
			boardcheck(x,y)
		if board[y][x] == 1:
			image.putpixel((x,y),(255,255,255))
print(*board)

image.save("maze.png","PNG")