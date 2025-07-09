import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("Original", img)

#horizontol
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)

#vertical

ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)












































