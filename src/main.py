import cv2
import time
import os
from util import img_processing as imgp
from util import cv_processing as cvp
from util import pil_processing as pilp

video_path = './media/name.mp4'

cap = cv2.VideoCapture(video_path)

cap.set(cv2.CAP_PROP_POS_FRAMES, 400)
success, frame = cap.read()

while True:
    success, frame = cap.read()
    if success:
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        break
    else:
        break

cap.release()
cv2.destroyAllWindows()