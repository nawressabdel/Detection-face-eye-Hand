import cv2
import random
from random import randrange
import mediapipe as np
import time

neuronesFace = cv2.CascadeClassifier('C:\Program Files\hardscade_face.xml')
neuronesEye = cv2.CascadeClassifier('C:\Program Files\haarcascade_eye.xml')

pastTime = 0
presentTime = 0
vid = cv2.VideoCapture('C:\Program Files\Inspiring Tunisia - Shot on RED.mp4')

npHands = np.solutions.hands
hands = npHands.Hands()
handDraw = np.solutions.drawing_utils

while True:
    read, video = vid.read()
    vidRGB = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
    detcR = hands.process(vidRGB)
    print(detcR.multi_hand_landmarks)
    video_frame_read, frame = vid.read()
    black_frame_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_neurones = neuronesFace.detectMultiScale(black_frame_video)
    eye_neurones = neuronesEye.detectMultiScale(black_frame_video)
    print(face_neurones)
    for (x, y, w, h) in face_neurones:
          cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
    for (x, y, w, h) in eye_neurones:
           cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 1, 150), 5)
           cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
          break
    if detcR.multi_hand_landmarks:
        for handl in detcR.multi_hand_landmarks:
            for Fid, Ln in enumerate(handl.landmark):
              w, h, c = video.shape
              cx, cy = int(Ln.x*w), int(Ln.y*h)
              print(Fid, cx, cy)
              if Fid == 10:
                    cv2.circle(video, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

        handDraw.draw_landmarks(video, handl, npHands.HAND_CONNECTIONS)
        presentTime = time.time()
        speed = 1/(presentTime - pastTime)
        presentTime = pastTime
        cv2.putText(video, str(speed), (5, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("pp", video)
    cv2.waitKey(1)


