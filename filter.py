#https://www.geeksforgeeks.org/working-images-python/

from PIL import Image
import random
import sys
origin = Image.open(sys.argv[1])
imgx, imgy = origin.size
filtered = Image.new("RGB", (imgx, imgy))
posx = 9/20
posy = 1/3

for x in range(imgx):
	for y in range(imgy):
		r,g,b = origin.getpixel((x,y))
		"""
		cross vin
		rnew = r-int(abs((x-imgx/2)*(y-imgy/2))/(imgx/2))
		gnew = g-int(abs((x-imgx/2)*(y-imgy/2))/(imgx/2))
		bnew = b-int(abs((x-imgx/2)*(y-imgy/2))/(imgx/2))
		
		diag vin
		rnew = r-int(abs((x-imgx/2)+(y-imgy/2)))
		gnew = g-int(abs((x-imgx/2)+(y-imgy/2)))
		bnew = b-int(abs((x-imgx/2)+(y-imgy/2)))

		norm vin
		rnew = r-int((abs(x-imgx/2)+abs(y-imgy/2))*.4)
		gnew = g-int((abs(x-imgx/2)+abs(y-imgy/2))*.4)
		bnew = b-int((abs(x-imgx/2)+abs(y-imgy/2))*.4)

		sepia
		rnew += 50
		bnew -= 50

		less contrast and lighter (flat tone)
		rnew = int((255-r)/3+r)
		gnew = int((255-g)/3+g)
		bnew = int((255-b)/3+b)

		increased contrast
		rnew = int(r-(255-r)+30)
		gnew = int(g-(255-g)+30)
		bnew = int(b-(255-b)+30)

		Sepia tone
		rnew = int(r-(255-r)+50)
		gnew = int(g-(255-g)+50)
		bnew = int(b-(255-b)+50)
		rnew += 50
		bnew -= 50
		rnew -= int((abs(x-imgx/2)+abs(y-imgy/2))*.4)
		gnew -= int((abs(x-imgx/2)+abs(y-imgy/2))*.4)
		bnew -= int((abs(x-imgx/2)+abs(y-imgy/2))*.4)
		rnew += random.randint(0,20)
		gnew += random.randint(0,20)

DOGGO COMPLETE
		rnew = int(r-(255-r)+180)
		gnew = int(g-(255-g)+180)
		bnew = int(b-(255-b)+180)
		rnew += 50
		bnew -= 50
		rnew -= int((abs(x-imgx*posx)+abs(y-imgy*posy))*.1)
		gnew -= int((abs(x-imgx*posx)+abs(y-imgy*posy))*.1)
		bnew -= int((abs(x-imgx*posx)+abs(y-imgy*posy))*.1)
		rnew += random.randint(0,10)
		gnew += random.randint(0,10)
	
DOGGO WATER NEAR COMPLETE AND WATER TOWER NEAR COMPLETE
		if r > 204:
			rnew = 255
		elif r > 153:
			rnew = 190
		elif r > 102:
			rnew = 130
		elif r > 51:
			rnew = 60
		else:
			rnew = 0

		if b > 204:
			bnew = 255
		elif b > 153:
			bnew = 190
		elif b > 102:
			bnew = 130
		elif b > 51:
			bnew = 60
		else:
			bnew = 0

		if g > 204:
			gnew = 255
		elif g > 153:
			gnew = 190
		elif g > 102:
			gnew = 130
		elif g > 51:
			gnew = 60
		else:
			gnew = 0
"""
		if b > 204:
			bnew = 255
		elif b > 153:
			bnew = 190
		elif b > 102:
			bnew = 130
		elif b > 51:
			bnew = 60
		else:
			bnew = 0
		rnew = r
		if g > 204:
			gnew = 255
		elif g > 153:
			gnew = 190
		elif g > 102:
			gnew = 130
		elif g > 51:
			gnew = 60
		else:
			gnew = 0


		filtered.putpixel((x,y),(rnew,gnew,bnew))


filtered.save("filtered.png","PNG")