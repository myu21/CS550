import sys
x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
if float(x)<float(y):
	if float(y)<float(z):
		print("True")
	else:
		print("False")
else:
	if float(y)>float(z):
		print("True")
	else:
		print("False")