import random as r
import matplotlib.pyplot as plt
data = []
n = 1000000

for z in range(n):
	for x in range(r.randint(1,13)):
		totalcal = 0
		for y in range(r.randint(1,15)):
			totalcal += r.randint(40,500)
	exists = 0
	while exists == 0:
		try:
			data[totalcal]
		except IndexError:
			data.append(0)
		else:
			break
	data[totalcal] += 1

plt.plot(data)
plt.show()