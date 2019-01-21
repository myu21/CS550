"""
1.21.2019
Monte-Carlo simulation project
Mitchell Yu
Question: How many erasers will you buy in a lifetime?
NOTES: if you want to, you can actually change some of the values like carelessness or lifespan to values that you think will represent your own values. Then the output will have a smaller range, giving you a better answer.
On my honor
"""
import random as r
import matplotlib.pyplot as plt
data = []
n = 100000

for z in range(n):
	print(n-z)
	erasernum = 0
	lifespan = r.randint(0,31046) # age range of 15-100 as days rather than years. I decided 15 years old is when people can start buying erasers. While 122 years old was the oldest person ever, I can't picture anyone over the age of 100 actively using erasers on a daily basis.
	carelessness = r.randint(30, 73) # maximum number of days before the eraser will be lost. I set it at two years, assuming that visibility is a 10, which this variable will be multiplied by.
	coef_eraser = 3.65 # assuming the eraser is never lost, and the size and effectiveness of the eraser are the average, then this would be the coefficient nessessary to make the eraser last a full year.
	while lifespan > 0:
	# Eraser Survival
		size = r.randint(10,20) # to understand the units here, 1 represents the size of the eraser on the back of a pencil, while 10 represents the size of a normal eraser. I have decided that I would not include 1 in the size becuase no one would buy a pencil just to use the eraser on the back of it. Instead, the size is just a unit to help give meaning to the larger number. For example, a 20 would be 20 times the size of the eraser on a back of a pencil
		effectiveness = r.randint(5,15) # a 10 eraser would be normally effective, while 5 while loose rubber really fast and 15 would maintain rubber really well
		eraserlife = size*effectiveness*coef_eraser
	# Pack information
		packnum = r.randint(1,6) # this represents the number of erasers per pack bought
		erasernum += packnum
		packused = r.randint(1,packnum) # this represents the number of erasers that are actually used from every box bought (sometimes erasers are bought in bulk, but not all of them end up getting used before buying the next pack, but even though these extra erasers are never used, you technically bought them)
	# Eraser misplacement probability
		visibility = r.randint(1, 15) # the visibility of the eraser. If the eraser is black, then it would be far easier to lose than a glow in the dark neon green eraser. 1 represents the lowest visibility while 15 represents the highest visibility
		# for the carelessness component scroll to the top
		maxdays = carelessness*visibility # maximum number of days before the eraser inevitably disapears
		for x in range(packused):
			while eraserlife > 0 and maxdays > 0:
				vigor = (r.randint(0,20))/10 # decided that the maximum worth days you can do of erasing within one day would be two days of erasing in one day
				lifespan -= 1
				eraserlife -= vigor
				maxdays -= 1
	while True:
		try:
			data[erasernum]
		except IndexError:
			data.append(0)
		else:
			break
	data[erasernum] += 1

plt.plot(data)
plt.show()