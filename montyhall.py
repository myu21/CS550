"""
1.9.2019
Monty Hall HW
Mitchell Yu
On My Honor
"""

import random as r
wincountstay = 0
wincountswitch = 0
for x in range(1000):
	car = r.randint(0,2)
	choose = r.randint(0,2) # there is no need to code which option was the one taken away/revealed (refer to comment on line 17)
	if choose == car:
		wincountstay += 1
	else:
		wincountswitch += 1 # if the car is not in the initial option, then that is an automatic win for the switched option because the choice to switch would result in the second option being chosen
print("Percentage of wins without changing boxes: "+str(wincountstay/10)) # the code still runs 1000 times for each, but I decided that it would be easier to understand the data if it is displayed as a percentage of wins out of 1000 times
print("Percentage of wins when changing boxes: "+str(wincountswitch/10))

"""
So after running the program a few times, it is apparent that staying would result in winning 1/3 times while switching would result in winning 2/3 times. This is because when the first choice is chosen, there is a 1/3 chance of winning. This means that the remaining two options represent the 2/3 chance of winning left. Once one of the two remaining options is revealed not to be the prize, the option still represents the same chance. The probability of winning does not change after one option is revealed, rather the remaining choice remains with a 2/3 chance of winning, making switching to this option a better choice than staying with a 1/3 chance of winning. (The youtube channel "Numberphile" has a video that explained this nicely: https://www.youtube.com/watch?v=4Lb-6rxZxx0)
"""