import cv2
import numpy as np

def cross(x):
    if s1==0:
        img[:]=0
    else:
        img[:]=(b,g,r)

img=np.zeros((600,500,3),np.uint8)
cv2.namedWindow("Color Picker")
s="0:OFF\n1:ON"

cv2.createTrackbar(s,"Color Picker",0,1,cross)

cv2.createTrackbar("B","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("R","Color Picker",0,255,cross)


while True:
    cv2.imshow("Color Picker",img)
    if cv2.waitKey(1) & 0xFF == 13:
        break
    
    s1=cv2.getTrackbarPos(s,"Color Picker")
    b=cv2.getTrackbarPos("B","Color Picker")
    g=cv2.getTrackbarPos("G","Color Picker")
    r=cv2.getTrackbarPos("R","Color Picker")
    
    
    
cv2.destroyAllWindows()