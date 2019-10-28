# extract and plot each detected face in a photograph
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
 
from os import listdir
from os.path import isfile, join

# draw each face separately
def draw_faces(filename, result_list, imageName):
	# load the image
	data = pyplot.imread(filename)
	count=0
	# plot each face as a subplot
	for i in range(len(result_list)):
		# get coordinates
		x1, y1, width, height = result_list[i]['box']
		x2, y2 = x1 + width, y1 + height
		# define subplot
		pyplot.subplot(1, len(result_list), i+1)
		pyplot.axis('off')
		# plot face
		# pyplot.imshow(data[y1-60:y2+60, x1-60:x2+60])
		try:
			pyplot.imshow(data[y1-60:y2+60, x1-60:x2+60])
			pyplot.savefig('TestResult/'+str(count) + imageName, bbox_inches="tight")
			count=count+1
			pyplot.close()
			# data = pyplot.imread(filename)
		except:
			try:
				pyplot.imshow(data[y1-40:y2+40, x1-40:x2+40])
			except:
				try:
					pyplot.imshow(data[y1-20:y2+20, x1-20:x2+20])
				except:
					try:
						pyplot.imshow(data[y1:y2, x1:x2])
					except:
						print('Negative coordinates ' + imageName)
		# pyplot.imshow(data[y1:y2, x1:x2])
	# show the plot
	# pyplot.savefig('FirstResult/'+imageName, bbox_inches="tight")
	# pyplot.close()
	# pyplot.show()
 
mypath='Test'
images = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# filename = 'sample/test3.jpg'


for image in images:	
	filename='Test/'+image
	# load image from file
	pixels = pyplot.imread(filename)
	# create the detector, using default weights
	detector = MTCNN()
	# detect faces in the image
	faces = detector.detect_faces(pixels)
	# display faces on the original image
	draw_faces(filename, faces, image)