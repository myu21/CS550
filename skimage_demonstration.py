"""
Mitchell Yu
1/30/2019
Example code for SciKit-Image Toolkit
On My Honor
Resources: scikit-image.org
Three examples: Corner detection, swirl transformation, region boundries
"""

# Example 1 - Corner detection of black and white image

from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.color import rgb2gray
from skimage.transform import resize

image = mpimg.imread("polygon.jpg") # imports photo as a NumPy array
image = resize(image,(200, 200)) # resize image to fit axis
image = rgb2gray(image) # convert color image to grayscale

coords = corner_peaks(corner_harris(image), min_distance=1) # finds corner a minimum of 1 unit away from another corner
coords_subpix = corner_subpix(image, coords, window_size=9) # within a window size (9 in this case), sees the varience in grayscale to determin whether the corner is truely a corner

fig, ax = plt.subplots() # creates plot
ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray) # displays image in background of plot
ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=10) #plotting the spots where both values concide into a corner
ax.axis((0, 200, 200, 0)) # setting values for the plot dimensions
plt.show() # displays whole piece together

#-------------------------------------------------------------------------------------------------

# Example 2 - Transforming image with swirl

from skimage.transform import swirl

image2 =  mpimg.imread("polygon.jpg") # imports photo as a NumPy array
image2 = resize(image2,(200, 200)) # resize image to fit axis
image2 = swirl(image2, rotation=0, strength=10, radius=90)  # swirling image2

fig, ax1 = plt.subplots() # creates plot
ax1.imshow(image2, cmap=plt.cm.gray, interpolation='none') # displaying image on plot
ax1.axis('off') # removing axis and labels
plt.show() # displaying whole piece

#-------------------------------------------------------------------------------------------------

# Example 3 - Creating region boundries around a photo of a cat

from skimage.future import graph
from skimage import segmentation, color, filters, io

image3 = mpimg.imread("cat.jpg") # import photo as NumPy array
imagegray = color.rgb2gray(image3) # converts photo to grayscale

outline = segmentation.slic(image3, compactness=50, n_segments=1000) # takes grayscaled image and outlines it
imagecolor = color.gray2rgb(imagegray) # converts grayscale image to colored (based on intensity of brightness and darkness)

g = graph.rag_boundary(outline, imagegray) # combined graphic broundries
lc = graph.show_rag(outline, g, imagecolor, img_cmap=None, edge_cmap='viridis', edge_width=1) # graph itself combining color with outline, creating colored outline
io.show() # display