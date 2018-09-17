#https://en.wikipedia.org/wiki/Zeller%27s_congruence
#I tried to use the formulas you gave me, but it didn't seem to work, so I instead used Zellers congruence
#To be honest, Zellers congruence isn't very accurate either. Sometimes it hits the mark dead on, and sometimes its just off by a few days
#I guess the most accurate system would just take a known day and use simple subtraction to find the day of the week

import sys
m = sys.argv[1]
d = sys.argv[2]
y = sys.argv[3]
l = float(y)%1000 #last two digits of the year
f = int(float(y)/100) #first two digits of the year (century)
if float(m)<3:
	m = float(m)+12
w = (float(d)+((13*float(m)-1)/5)+float(l)+(float(l)/4)+(float(f)/4)-2*float(f))%7

if w < 7:
	if w < 6:
		if w < 5:
			if w < 4:
				if w < 3:
					if w < 2:
						if w < 1:
							day = "Sunday"
						else:
							day = "Monday"
					else:
						day = "Tuesday"
				else:
					day = "Wednesday"
			else:
				day = "Thursday"
		else:
			day = "Friday"
	else:
		day = "Saturday"

print("The day of the week is: "+day)
