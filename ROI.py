import cv2


img=cv2.imread("E:\\jeff.jpg")

#img=cv2.resize(img,(800,800))


#(209,11),(408,255)
#244 #199
#roi=img[11:255,209:408]

#img[11:255,409:608]=roi
#img[11:255,9:208]=roi
#img[256:500,9:208]=roi
#cv2.imwrite("E:\\Jeff1.jpg",img)

img=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=[255,0,125])
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()