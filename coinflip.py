import random as r
import matplotlib.pyplot as plt

data = [0]*11
trialnum = 10000

for x in range(trialnum):
	coincounter = 0
	for y in range(10):
		coin = r.randint(0,1)
		if coin == 1:
			coincounter += 1
	data[coincounter] += 1
print(data)
"""
display = [0 for i in range(11)]
for i in range(len(data)):
	display[data[i]] += 1
"""
plt.bar([0,1,2,3,4,5,6,7,8,9,10], data, color=(.5,0,.5,1))
plt.show()