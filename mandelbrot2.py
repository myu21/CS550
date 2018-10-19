"""
Mitchell Yu
Mandelbrot 2
Based on Ms. Healey's
On my honor

"""
from PIL import Image

xa, xb = 0.2850579965743236,0.2869347193627618
ya, yb = -0.01226480008335784,-0.01038807729491964
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
		r = 20
		g = 20
		b = i

		image.putpixel((x,y),(r,g,b))

image.save("mandelbrot2.png","PNG")