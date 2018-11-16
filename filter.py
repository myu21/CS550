"""
Mitchell Yu
Photo filter challenge
16 November 2018
This filter applies vignetting, a sepia color tone, and a higher contrast.
On my honor
"""

from PIL import Image
import random
import sys
origin = Image.open(sys.argv[1])
imgx, imgy = origin.size
filtered = Image.new("RGB", (imgx, imgy))
posx = 9/20 # position of main object so everything around it will get darker
posy = 1/3

for x in range(imgx):
	for y in range(imgy):
		r,g,b = origin.getpixel((x,y))
		
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

		filtered.putpixel((x,y),(rnew,gnew,bnew))

filtered.save(sys.argv[1]+"_filtered.png","PNG")