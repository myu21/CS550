"""
Mitchell Yu
Challenge Question Lists HW
I did the first one (by Ms. Healey), the third one (by Anjali, Sonali, and Mia), and the last one (by Kaki, Stephanie, Alex, and Daniel)
"""

import random as r

num = []
hold = 0
for x in range(10):
	num.append(r.randrange(100))
for x in range(10):
	if num[x]%3 == 0:
		hold += 1
		num.insert(0, num.pop(x))
for y in range(hold):
	del num[0]
print(sorted(num, reverse=True))

num2 = []
for x in range(15):
	num2.append(r.randrange(100))
while True:
	user = input("Please input a number between 0 and 100\n>>")
	if int(user)<=100 or int(user)>=0:
		break
num2.append(int(user))
print(sorted(num2, reverse=True))

num3 = []
base = input("PLease input your desired base\n>>")
exp = input("Please input your desired exponent\n>>")
for x in range(int(exp)):
	num3.append(int(base)**x)
print(num3)
