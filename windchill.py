import sys

t = sys.argv[1]
v = sys.argv[2]
w = 35.74 + 0.6215*float(t)+(0.4275*float(t)-35.75)*(float(v)**0.16)
print("Wind Chill is "+str(w))