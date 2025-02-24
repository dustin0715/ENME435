import numpy as np
import matplotlib
import imutils
import cv2

image = cv2.imread("testudo.jpg")
print("Original image shape:", image.shape)

# image2 = imutils.resize(image, width=400)
# print("Resize image shape:", image2.shape)

# cv2.imwrite("02182025_testudo.jpg", image2)
slice = image[0:200, 0:350]
cv2.imshow("Slice", slice)

image[100:200, 150:300] = (254, 78, 10)

cv2.imshow("Caption here",image)
# cv2.imshow("Resized Testudo",image2)
# Without the below line, image appears and disappears extremely quick. 
# This line keeps the image appear until user hit a key
cv2.waitKey(0) 