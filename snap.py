from cv2 import cv2
import cvzone
import cvt
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cascade = cv2.CascadeClassifier(r"C:\\users\\Zaineb\\PycharmProjects\\pythonProject2\\haarcascade_frontalface_default.xml")
overlay = cv2.imread('beard.png',cv2.IMREAD_UNCHANGED)
while True:
    frame: object
    _,frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)

    for(x,y,w,h) in faces:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        overlay_resize = cv2.resize(overlay,(int(w*1.5),int(h*1.5)))
        frame = cvzone.overlayPNG(frame,overlay_resize,[x-45,y-75])
    cv2.imshow('snap', frame)
    if cv2.waitKey(10) == ord('q'):
        break

