"""
1.11.2019
Dart HW
Mitchell Yu
On My Honor
The longest walk is 22 blocks. 22 blocks will ensure that you will walk home around 51% of the time. I used to think it was 14, because 15 would produce 49% so it would have to be one lower than that, but then I realized that whether the number was even or odd would drastically affect the percentage. Even numbers would end closer in general to the origin than oddd numbers. I wrote a program that tested 50 different distances at once and displayed them all. From this, I found that 22 blocks was the closest one to 50%.
Monte Carlo Simulation (aka probability simulation)
What are they? They are simulations used to model the probability of different outcomes of a process that is hard to predict due to the randomness of varibles. They rely on repeated random sampling to find probability
What can they be used for? Virtually anything invloving data and random variables hard to predict - Science, engineering, finance, law, statistics, art, graphics, etc.
How do they work? A function with a degree of randomness produces values which are then catagorized by its probability of showing up over many trials. 
"""
import random as r
for x in range(2,5):
	n = 10**x
	hit = 0
	for x in range(n):
		xvalue = ((r.randint(0,1000))/1000)-1
		yvalue = ((r.randint(0,1000))/1000)-1
		if ((xvalue**2)+(yvalue**2))**(1/2) <= 1: # used pythagorean theorem to find distance from origin. Since the circle is a unit circle, any value over one would not be in the circle.
			hit += 1
	output = (hit*4)/n
	print(output)
# the output approaches around 3.14-ish as the trial numbers get greater and greater