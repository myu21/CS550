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
		rnew = b
		bnew = r
		gnew = 130

		filtered.putpixel((x,y),(rnew,gnew,bnew))

filtered.save(sys.argv[1]+"_filtered2.png","PNG")