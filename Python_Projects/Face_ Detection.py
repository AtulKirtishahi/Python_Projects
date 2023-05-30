import cv2


face_cap = cv2.CascadeClassifier('C://Users//atulk//anaconda3//Lib//site-packages//cv2//data//haarcascade_frontalface_default.xml')
enable_cam = cv2.VideoCapture(0)

while True :
    read_img , mp4 = enable_cam.read()
    
    Cl = cv2.cvtColor(mp4,cv2.COLOR_BGR2GRAY)
    face = face_cap.detectMultiScale(
            Cl,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30,30),
            flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in face:
        cv2.rectangle(mp4, (x + w, y + h), (x, y), (0, 255, 0), 2)

    
    cv2.imshow('video_live', mp4)
    
    if cv2.waitKey(5) == ord('a'):
        break


enable_cam.release()
