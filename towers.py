number = int(input("Input number of discs"))

def moves(n, left):
	if n == 0:
		return
	moves(n-1, not left)
	if left:
		print(str(n)+'left')
	else:
		print(str(n)+'right')
	moves(n-1, not left)

moves(number, True)
"""
The number next to each move is directly related to the size. All of the even numbered discs move one direction and the odds in the other (so it is alternating).

The general pattern is that all the odds and evens are paired with the same command(left or right), and that the numbers are "sandwiched together"
ex:
1,2,1
1,2,1,3,1,2,1
1,2,1,3,1,2,1,4,1,2,1,3,1,2,1

Tracing:
moves(3, True)
	moves(3-1, not left (left false))
		moves(2-1, not left (left true))
			moves(1-1, not left (left false))
				if n == 0:
					return
			if left:
				print(str(1)+'left')
			moves(1-1, not left (left false))
				if n == 0:
					return
		else:
			print(str(2)+'right')
		moves(2-1, not left (left true))
			moves(1-1, not left (left false))
				if n == 0:
					return
			if left:
				print(str(1)+'left')
			moves(1-1, not left (left false))
				if n == 0:
					return
	if left:
		print(str(3)+'left')
	moves(3-1, not left (left false))
		moves(2-1, not left (left true))
			moves(1-1, not left (left false))
				if n == 0:
					return
			if left:
				print(str(1)+'left')
			moves(1-1, not left (left false))
				if n == 0:
					return
		else:
			print(str(2)+'right')
		moves(2-1, not left (left true))
			moves(1-1, not left (left false))
				if n == 0:
					return
			if left:
				print(str(1)+'left')
			moves(1-1, not left (left false))
				if n == 0:
					return
output:
1left
2right
1left
3left
1left
2right
1left

"""