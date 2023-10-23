import cv2 as cv
img= cv.imread(r"C:\Users\Lenovo\PycharmProjects\OCR\istockphoto-155355209-612x612.jpg")
gray_img=cv.cvtColor(img , cv.COLOR_BGR2GRAY)

face=cv.CascadeClassifier(r"haarcascade_frontalface_default.xml")
face_rect=face.detectMultiScale(gray_img,1.1,9)

for (x,y,w,h) in face_rect:
    cv.rectangle(img , (x,y),(x+w, y+h) , (0, 255,0),2)

cv.imshow("face detected",img)
cv.waitKey(0)