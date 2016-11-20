import sys
import math
import opencv as cv2
import numpy as np
from matplotlib import pyplot as plt

numimages = 26 # max image number
imgnum = 1 # keeps track of which image we're on
thresh = 50 # minimum distance from average sand color to be marked as not sand

def keypress(event):
	if event.key == 'escape': # exit
		plt.close()
		sys.exit()

	global imgnum, thresh
	sys.stdout.flush()

	if event.key == 'right' or event.key == 'down': # scroll forward one image
		imgnum = min(imgnum+1, numimages)
	if event.key == 'left' or event.key == 'up': # scroll backward one image
		imgnum = max(imgnum-1, 1)
	if event.key == 'q': # decrement minimum edge threshold by 10
		thresh = thresh - 5
	if event.key == 'w': # increment minimum edge threshold by 10
		thresh = thresh + 5
	if event.key == '1': # decrement minimum edge threshold by 50
		thresh = thresh - 10
	if event.key == '2': # increment minimum edge threshold by 50
		thresh = thresh + 10
		
	plot(imgnum, thresh) # reload image

def detect(img, thresh):
	height = np.size(img, 0)
	width = np.size(img, 1)
	sand = [(194, 178, 128)]
	new_image = np.zeros((height,width,3), np.uint8)
	
	for i in range(height):
		for j in range (width):
			px = img[i,j]
			dist = math.sqrt(math.pow((px[0] - sand[0]),2) + math.pow((px[1] - sand[1]),2) + math.pow((px[2] - sand[2]),2))
			if dist > thresh:
				new_image[i,j] = [255,255,255]
				
	return new_image

def plot(imgnum, thresh): # min and max thresholds on gradient steepness
	global numimages

	img = cv2.imread('sample_images/'+str(imgnum)+'.jpg')
	# If you want you can change this directory to sample_images (the ones taken
	# at the beach), but the images in there are so large that edge detection
	# becomes less useful (try it out and see).
	# My gut feeling is that the more compressed the image, the more useful edges are.

	result = detect(img, thresh)

	plt.subplot(121),plt.imshow(img,cmap = 'gray')
	plt.title('Original Image ('+str(imgnum)+' of '+str(numimages)+')'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(result,cmap = 'gray')
	plt.title('New Image ('+str(thresh)+')'), plt.xticks([]), plt.yticks([])

	plt.draw()
	
plt.figure().canvas.mpl_connect('key_press_event', keypress)
plot(imgnum, thresh)
plt.show()