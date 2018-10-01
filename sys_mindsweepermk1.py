"""
Mitchell Yu
Mindsweeper HW # 1
Still working on the edge problem
"""
import random
import sys

width = int(sys.argv[1])
height = int(sys.argv[2])
bomb = int(sys.argv[3])
board = []

board = [[0]*width for x in range(height)]

for x in range(bomb):
	board[random.randint(0, height-1)][random.randint(0, width-1)] = "*"
for x in range(width):
	for y in range(height):
		z = 0
		try:
			if board[y][x-1] == "*" and x-1>=0:
				z += 1
			if board[y][x+1] == "*":
				z += 1
			if board[y-1][x] == "*" and y-1>=0:
				z += 1
			if board[y+1][x] == "*":
				z += 1
			if board[y-1][x-1] == "*" and y-1>=0 and x-1>=0:
				z += 1
			if board[y+1][x-1] == "*" and x-1>=0:
				z += 1
			if board[y-1][x+1] == "*" and y-1>=0:
				z += 1
			if board[y+1][x+1] == "*":
				z += 1
		except IndexError:
			continue
		if board[y][x] != "*":
			board[y][x] = z


for x in range(len(board)):
	print(*board[x])