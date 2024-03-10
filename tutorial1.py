import cv2

img = cv2.imread('assets/IMG_2163.PNG', -1) # load image

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # resize image to half the size
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.PNG', img) # saving image to file

cv2.imshow('Image', img) # show image in window named "Image"
cv2.waitKey(0) # wait infinite amount of time to destory image until key is pressed (int: seconds until closed)
cv2.destroyAllWindows()