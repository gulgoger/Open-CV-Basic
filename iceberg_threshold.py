import cv2

def nothing(x):
    pass

cv2.namedWindow("Iceberg Threshold Trackbar")
cv2.createTrackbar("lower","Iceberg Threshold Trackbar",0,255,nothing)
cv2.createTrackbar("upper","Iceberg Threshold Trackbar",0,255,nothing)

img = cv2.imread("C:\\Users\\asus_\\Documents\\Projects\\OPENCV\\test_images\\iceberg.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    lower = cv2.getTrackbarPos("lower","Iceberg Threshold Trackbar")
    upper = cv2.getTrackbarPos("upper","Iceberg Threshold Trackbar")
    ret,threshold = cv2.threshold(gray,lower,upper,cv2.THRESH_BINARY)

    cv2.imshow("Iceberg-Threshold",threshold)

cv2.destroyAllWindows()
