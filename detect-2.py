# face detection with mtcnn on a photograph
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN

from PIL import Image
 
from os import listdir
from os.path import isfile, join
 
# draw an image with detected objects
def draw_image_with_boxes(filename, result_list, image, extension, dateInfo):
	delimeter='&'
	# load the image
	data = pyplot.imread(filename)
	# plot the image
	pyplot.imshow(data)
	# get the context for drawing boxes
	ax = pyplot.gca()
	count=0
	# pyplot.axis('off')
	# plot each box
	for result in result_list:
		pyplot.axis('off')
		# get coordinates
		x1, y1, width, height = result['box']
		x2, y2 = x1 + width, y1 + height
		if(x1 < 0):
			x1=0
		
		if(y1 < 0 ):
			y1=0

		try:
			pyplot.imshow(data[y1-60:y2+60,x1-60:x2+60])
		except:
			try:
				pyplot.imshow(data[y1-40:y2+40,x1-40:x2+40])
			except:
				try:
					pyplot.imshow(data[y1-20:y2+20,x1-20:x2+20])
				except:
					pyplot.imshow(data[y1:y2,x1:x2])
		pyplot.savefig('ThirdResult/' + image + delimeter + str(count) + delimeter + dateInfo + '.' + extension, bbox_inches="tight")
		pyplot.close()
		count=count+1

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]
 
mypath = 'Third'

images = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for image in images:	
	filename='Third/'+image
	# load image from file
	pixels = pyplot.imread(filename)
	# create the detector, using default weights
	detector = MTCNN()
	# detect faces in the image
	faces = detector.detect_faces(pixels)
	date=get_date_taken(filename)

	parts=str.split(date, ' ')
	parts[0]=parts[0].replace(':', '-')
	parts[1]=parts[1].replace(':', '-')

	delimeter='&'
	dateinfo=parts[0] + delimeter + parts[1]

	imgParts = str.split(image, '.')

	# faces = list(filter(lambda x: x['confidence'] > 0.87, faces))

	# display faces on the original image
	draw_image_with_boxes(filename, faces, imgParts[0], imgParts[1], dateinfo)
