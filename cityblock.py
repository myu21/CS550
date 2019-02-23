import random as r
runnum = 10000

for n in range(50):
	walk = 0
	distance = []
	for y in range(runnum):
		xposition = 0
		yposition = 0
		for x in range(n):
			direction = r.randint(0,3)
			if direction == 0:
				yposition += 1
			if direction == 1:
				yposition -= 1
			if direction == 2:
				xposition += 1
			if direction == 3:
				xposition -=1
		distance.append(abs(xposition) + abs(yposition))
	for z in range(len(distance)):
		if distance[z] <= 4:
			walk+=1
	percentage = round(((walk/runnum)*100),1)
	print(percentage)