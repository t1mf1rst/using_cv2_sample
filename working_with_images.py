# library for processing images and videos
# installing opencv: pip install opencv-python
import cv2

# create image object: 1 - coloured image, 0 - black and white, -1 - coloured image with transparency
img = cv2.imread("galaxy.jpg", 1)

# python store image as N dimensional array
print( type(img) )

# show content of img
print( img )

# show size of it
print( img.shape )

# resize image
resized_image = cv2.resize( img, ( int(img.shape[0]/2), int(img.shape[1]/2) ) )
 # save new image
cv2.imwrite("galaxy_resized.jpg", resized_image)

# print image on the screen: 1) imshow(); 2) waitKey(0) where 0 - wait press key, 2000 - time in msec; 3) destroy windows on closing
cv2.imshow("Galaxy", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()