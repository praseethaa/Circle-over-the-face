import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("sasuke.jpg")
output = img.copy()
cir = circle_img = cv2.circle(img,(1050,175), 80, (0,0,250), 2)
cv2.putText(cir, "Uchiha Sasuke", (220, 350),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (225, 240, 0), 3)
cv2.imshow ("circle", circle_img )
cv2.imshow ("circle", cir ) 
cv2.waitKey(0)
