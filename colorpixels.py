"""
Mitchell Yu
Red Box
I created 10 columns that are red gradients
On my honor

"""

from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))

for x in range(imgx):
	for y in range(imgy):
		image.putpixel((x,y),((x*5)%255,0,0))

image.save("red_image.png","PNG")