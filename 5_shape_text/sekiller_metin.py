import cv2
import numpy as np

#resim olustur
img = np.zeros((512,512,3), np.uint8) #siyah bir resim zeroslardan olusuyor
print(img.shape)

cv2.imshow("Siyah", img)

#line
#resim, baslangıc noktası, bitis noktası, renk, kalınlık
cv2.line(img, (100,100), (100,300), (0,255,0),3)
cv2.imshow("Cizgi", img)

#rectangle
# resim
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Rectangle", img)

#circle
#resim, merkez, yarı çap, renk
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Circle", img)

#text
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Text", img)















