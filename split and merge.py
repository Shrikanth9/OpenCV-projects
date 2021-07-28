import cv2
import numpy as np


img=cv2.imread("E:\\jeff.jpg")
cv2.imshow("Original",img)
print("Shape==",img.shape)
print("Pixels==",img.size)
print("Datatype==",img.dtype)
print("Imagetype==",type(img))

b,g,r=cv2.split(img)
"""
print("Blue==",b)
print("Green==",g)
print("Red==",r)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
"""
mr1=cv2.merge((r,g,b))
cv2.imshow("Merged",mr1)

cv2.waitKey(0)
cv2.destroyAllWindows()