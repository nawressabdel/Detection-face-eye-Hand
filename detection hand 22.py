import mediapipe as mp
import time
import cv2

vid = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpdraw = mp.solutions.drawing_utils

pastTime = 0
presentTime = 0






while True:
    read, video = vid.read()
    RGB_vid = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)

    print(RGB_vid)
    resultat = hands.process(RGB_vid)
    if resultat.multi_hand_landmarks:
        for Handlandmarks in resultat.multi_hand_landmarks:
            for FingerId , fingerLandmark in enumerate(Handlandmarks.landmark):
                print(FingerId, fingerLandmark)
                h, w, c = video.shape
                cx, cy = int(fingerLandmark.x*w), int(fingerLandmark.y*h)
                print(FingerId, cx, cy)

cv2.circle(video, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
mpdraw.draw_landmarks(video, Handlandmarks, mpHands.HAND_CONNECTIONS)
presentTime=time.time()
detectionspeed = 1/(presentTime-pastTime)
pastTime = presentTime
cv2.putText(video, str(int(detectionspeed)), (15, 75), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 3)



cv2.imshow("fenetre", video)
cv2.waitKey(0)
