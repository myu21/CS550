"""
Mitchell Yu
Stars in the sky
(Julia Set)
I was messing around with the Julia Set, and I found that a lot of them looked very "nebula-like". I decided to go with this theme and also put the stars in the background
No sources
On my honor

"""

from PIL import Image
import random

xa, xb = -1.7,1.7
ya, yb = -1.7,1.7
imgx, imgy = 1000, 1000
maxIt = 256
exp = 2
c = complex(.4, .5)

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y*((yb-ya)/(imgy-1))+ya
	for x in range(imgx):
		cx = x*((xb-xa)/(imgx-1))+xa
		z = complex(cx, cy)
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**exp+c
		j = random.randint(0,700)
		if j<1:
			k = random.randint(200,230)
			r= k
			g= k
			b=random.randint(150,200)
		else:
			r=i*10
			g=i*10
			b=i*8
		image.putpixel((x,y),(r,g,b))

image.save("stars_in_the_sky.png","PNG")