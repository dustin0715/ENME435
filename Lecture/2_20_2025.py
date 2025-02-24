import numpy as np
import matplotlib.pyplot as plt
import imutils
import cv2

# image = cv2.imread("testudo.jpg")

# blurred = cv2.blur(image, (21,21))

# blurred1 = cv2. GaussianBlur(image,(21,21),0)

# blurred2 = cv2.medianBlur(image,21)

# blurred3 = cv2.bilateralFilter(image,3,41,41)

# cv2.imshow("Average Blurred",blurred)
# cv2.imshow("Blurred",blurred3)

# cv2.imshow("Our old pal testudo",image)

canvas = np.zeros((500,500,3), dtype="uint8")
color = (50,200,100)
cv2.line(canvas,(0,0),(300,400),color,10)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0) 

