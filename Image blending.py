import cv2
import numpy as np



img1=cv2.imread("E:\\jeff.jpg")
img2=cv2.imread("E:\\jeff1.png")

img1=cv2.resize(img1,(500,700))
img2=cv2.resize(img2,(500,700))

def cross(x):
    pass

cv2.namedWindow("Trackbar")
img=np.zeros((600,500,3),np.uint8)
str1="0:OFF\n1:ON"
str2="Blend"
cv2.createTrackbar(str1,"Trackbar",0,1,cross)
cv2.createTrackbar(str2,"Trackbar",1,100,cross)

result=cv2.addWeighted(img1,1,img2,0,0)

while True:
    cv2.imshow("Trackbar",img)
    if cv2.waitKey(1) & 0xFF ==13:
        break

    a=cv2.getTrackbarPos(str1,"Trackbar")
    b=cv2.getTrackbarPos(str2,"Trackbar")
    if(a==0):
        cv2.imshow("Result",img)

        result=cv2.addWeighted(img1,1,img2,0,0)
    else:
        cv2.imshow("Result",result)
        result=cv2.addWeighted(img1,(1-(b/100)),img2,(b/100),0)
        cv2.putText(result,str(b),(20,50),cv2.FONT_ITALIC,2,(222,0,222),2)
      
        
cv2.destroyAllWindows()