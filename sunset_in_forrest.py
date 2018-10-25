"""
Mitchell Yu
Sunset in Forrest
I found that the edges of the mandelbrot when zoomed out would look like evergreens, so I simply took out the background and put in a gradient to create a sunset
No sources
On my honor

"""
from PIL import Image

xa, xb = -1.3760247685185185,-1.292893702846365
ya, yb = 0.03442907235939635,0.11756013803155002
imgx, imgy = 1000, 1000
maxIt = 256
exp = 2

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y*((yb-ya)/(imgy-1))+ya
	for x in range(imgx):
		cx = x*((xb-xa)/(imgx-1))+xa
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**exp+c
		if i<50:
			r = 0
			g = i
			b = 0
		else:
			r = 256
			g = (y+40)//2
			b = 0

		image.putpixel((x,y),(r,g,b))

image.save("sunset_in_forrest.png","PNG")