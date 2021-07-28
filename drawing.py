import cv2
import datetime

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("width==",cap.get(3))
print("height==",cap.get(4))

#fourcc=cv2.VideoWriter_fourcc(* 'XVID')
#output=cv2.VideoWriter("E:\\WEBCAM.avi",fourcc,30.0,(800,600))
while(cap.isOpened()):
    ret,image=cap.read()
    image=cv2.resize(image,(800,600))
    font=cv2.FONT_HERSHEY_COMPLEX_SMALL
    text='Height: ' + str(cap.get(4)) + ' Width: ' + str(cap.get(3))
    cv2.putText(image,text,(10,20),font,1,(0,155,255),1,cv2.LINE_AA)
    date_data="Date: " + str(datetime.datetime.now())
    cv2.putText(image,date_data,(10,50),font,1,(0,155,255),1,cv2.LINE_AA)
    cv2.imshow("VIDEO",image)
    #output.write(image)
    if cv2.waitKey(30) & 0xFF == ord("k"):
            break
cap.release()        
cv2.destroyAllWindows()