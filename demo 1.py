import cv2

vidcap=cv2.VideoCapture("E:\\Steve Rogers.mp4")
#ret,img=vidcap.read()
count=0;
while True:
     ret,img=vidcap.read()
     if ret==True:
        
         cv2.imwrite("F:\\frames\\imgN%d.jpg" %count,img)
         #vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        
         cv2.imshow("res",img)
         print(count)
         count+=1
         if cv2.waitKey(25) & 0xFF == ord("k"):
            break
            cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows()

#cv2.destroyAllWindows()
