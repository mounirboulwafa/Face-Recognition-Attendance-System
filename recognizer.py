import cv2
import numpy as np

import xlwrite
import firebase.firebase_ini as fire
import time
import sys
from playsound import playsound

start = time.time()
period = 8
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

flag = 0
id = 0
filename = 'filename'
dict = {
    'item1': 1
}
# font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 7)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id, conf = recognizer.predict(roi_gray)
        if conf < 50:
            if id == 1:
                id = 'Mounir Boulwafa'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 1, id, 'Yes')
                    dict[str(id)] = str(id)
                    print("Mounir Boulwafa")

            elif id == 2:
                id = 'Mohamed Jaafani'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 2, id, 'Yes')
                    dict[str(id)] = str(id)
                    print("Mohamed Jaafani")


            elif id == 3:
                id = 'Toufiq Boughname'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 3, id, 'Yes')
                    dict[str(id)] = str(id)
                    print("Toufiq Boughname")

            elif (id == 4):
                id = 'Imad Zaghdad'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 4, id, 'Yes');
                    dict[str(id)] = str(id)
                    print("Imad Zaghdad")

        else:
            id = 'Non reconnu'
            flag = flag + 1
            break

        cv2.putText(img, str(id) + " " + str(conf), (x, y - 10), font, 0.55, (120, 255, 120), 1)
        # cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('Frame', img)
    # cv2.imshow('gray',gray);

    # if flag == 10:
    #     print("Transaction Blocked")
    #     break
    if time.time() > start + period:
        break
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
