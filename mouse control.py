import cv2
import numpy as np

""""
def draws(event,x,y,flags,param):
     if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(124,0,0),2)
     if event == cv2.EVENT_RBUTTONDBLCLK:
         cv2.rectangle(img,(x,y),(x+100,y+75),(0,124,0),2)
 
cv2.namedWindow(winname="res")

img=np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",draws)

while True:
      cv2.imshow("res",img)
      if cv2.waitKey(1) & 0xFF==13:
          break
cv2.destroyAllWindows() """     


def draw(event,x,y,flags,param):
    print("event==",event)
    print("x==",x)
    print("y=",y)
    #print("flag==",flags)
    #print("param==",param)
    font=cv2.FONT_HERSHEY_PLAIN
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,' ,',y)
        cord="."+ str(x) + ','+ str(y)
        cv2.putText(img,cord,(x,y),font,1,(200,0,0),1)
       # cv2.imshow("image",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        pix="."+ str(b) + ',' + str(g) + ',' + str(r)
        cv2.putText(img,pix,(x,y),font,1,(0,200,0),1)
cv2.namedWindow(winname="res")
img=cv2.imread("E:\\jeff.jpg")
#img=np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",draw)

while True:
      cv2.imshow("res",img)
      if cv2.waitKey(1) & 0xFF==13:
          break
cv2.destroyAllWindows()