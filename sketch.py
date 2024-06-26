import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "elon.jpeg"

def rgb2gray(rgb):
    # using the 2d array formula to cinvert image to gray scale
    return np.dot(rgb[...,:3],[0.2989,0.5879,0.1140])

def dodge(front,back):
    final_sketch = front*255/(255-back)
    # if image is greater than 255 we convert it to 255
    final_sketch[final_sketch>255]=255
    final_sketch[final_sketch==255]=255
    return final_sketch.astype('uint8')

# to read the given img
s = imageio.imread(img)

gray = rgb2gray(s)

i = 255 - gray

# to blur the image 
blur = scipy.ndimage.filters.gaussian_filter(i,sigma = 15) # the sigma is the degree of blur

# this convert our image to sketch by taking two parameter as blur and grey
r = dodge(blur,gray)

# writing the image
cv2.imwrite('elon-sketch.png',r)