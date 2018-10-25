"""
Mitchell Yu
Coral
This is just a really weird abstract piece, I just called it coral beacuse that was what is resembled at the end
No sources
On my honor

"""
from PIL import Image

xa, xb = -0.2064153281680434,-0.20329504385129302
ya, yb = 0.6710557011695266,0.6741759854862769
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
		r=(i*5)%256
		b=(i*5)%256
		g=0
		if x>imgx/2 and y>imgy/2:
			r = 0
		image.putpixel((x,y),(r,g,b))

image.save("coral.png","PNG")