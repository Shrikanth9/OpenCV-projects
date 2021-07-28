#Screen recorder.....

import cv2
import pyautogui as p
import numpy as np

rs=p.size()

fn=input("Enter any file name and path:")
fps=20.0

fourcc=cv2.VideoWriter_fourcc(* 'XVID')
output=cv2.VideoWriter(fn,fourcc,fps,rs)

cv2.namedWindow("Live recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live recording",(600,400))


while True:
      img=p.screenshot()
      f=np.array(img)
      f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
      output.write(f)
      cv2.imshow("Live recording",f)
      if cv2.waitKey(1)== ord("k"):
            break
        
output.release()
cv2.destroyAllWindows()


