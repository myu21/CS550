"""
Mitchell Yu
Mandelbrot attempt 1
HW (10.19.2018)
On my honor

"""
from PIL import Image

imgx = 512
imgy = 512

mandelbrot = Image.new("RGB",(imgx, imgy))

for x in range(imgx):
	for y in range(imgy):
		shade = 0
		stop = 0
		zxcord = 0
		zycord = 0
		xcord = ((x/imgx)*4)-2
		ycord = ((y/imgy)*4)-2
		while True:
			if stop == 255:
				break
			zsquare1 = (zxcord**2)-(zycord**2)
			zsquare2 = 2*zxcord*zycord
			escape1 = zsquare1 + xcord
			escape2 = zsquare2 + ycord
			if ((escape1**2)+(escape2**2))**(1/2) > 2:
				break
				print("working")
			else:
				zxcord = escape1
				zycord = escape2
				shade += 1
				stop += 1
		mandelbrot.putpixel((x,y),(shade//2,0,shade))

mandelbrot.save("mandelbrot.png","PNG")
