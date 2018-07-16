import cv2, time

video = cv2.VideoCapture(0)

#
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
t = 0
while True:
	t = t+1
	check, frame = video.read()

	print(check)
	print(frame)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#time.sleep(1)

	#
	out.write(frame)

	cv2.imshow("Capturing", gray)

	key = cv2.waitKey(1)

	if key == ord('q'):
		break

print(t)

#
out.release()

video.release()
cv2.destroyAllWindows()