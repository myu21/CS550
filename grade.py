#Mitchell Yu
#September 17, 2018
#Grade HW
#I wanted to find a more elegent solution like assigning the letters and plus minus seperately, but I would still have to assign each letter seperately.

import sys
g = sys.argv[1]
g = float(g)

if g<0 or g>5:
	print("Please enter value between 0-5")
else:
	if g<=4.85:
		if g<=4.7:
			if g<=4.5:
				if g<=4.2:
					if g<=3.85:
						if g<=3.5:
							if g<=3.2:
								if g<=2.85:
									if g<=2.5:
										if g<=2:
											if g<=1.5:
												print("You Failed")
											else:
												print("D")
										else:
											print("D+")
									else:
										print("C-")
								else:
									print("C")
							else:
								print("C+")
						else:
							print("B-")
					else:
						print("B")
				else:
					print("B+")
			else:
				print("A-")
		else:
			print("A")
	else:
		print("A+")
