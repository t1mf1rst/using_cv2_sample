# this program detects human face from image
# it is get face model from xml file and try to find it in image
# you can download different object models from github - opencv/data/haarcascades
import cv2

# create searching object model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# load image 
img = cv2.imread("face1.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create var to store coordinates of rectangle with face
faces = face_cascade.detectMultiScale(gray_img,
	scaleFactor=1.165,
	minNeighbors=5)

for x, y, w, h in faces:
	img = cv2.rectangle( img, (x, y), (x + w, h + y), (0, 255, 0), 3 )

print( faces )

resized = cv2.resize( img, ( int(img.shape[1]/3), int(img.shape[0]/3) ) )

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()