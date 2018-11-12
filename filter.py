#https://www.geeksforgeeks.org/working-images-python/

from PIL import Image
import sys
origin = Image.open(sys.argv[1])
imgx, imgy = origin.size
filtered = Image.new("RGB", (imgx, imgy))

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


		sepia

		
		"""
		rnew = r-int((abs(x-imgx/2)+abs(y-imgy/2))*.4)
		gnew = g-int((abs(x-imgx/2)+abs(y-imgy/2))*.4)
		bnew = b-int((abs(x-imgx/2)+abs(y-imgy/2))*.4)

		rnew += 50
		bnew -= 50
		
		filtered.putpixel((x,y),(rnew,gnew,bnew))


filtered.save("filtered.png","PNG")