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

if success:
    # use the super resolution model to upscale the image, timing how
    # long it takes
    frame = cv2.resize(frame, (frame.shape[1]*4, frame.shape[0]*4))
    cv2.imwrite('bad.png', frame)
    
	# start processing
    start = time.time()
    frame = cvp.default_process(frame)
    end = time.time()
    print("[INFO] image processing took {:.6f} seconds".format(
	end - start))
    
    # write images to file
    cv2.imwrite('original1.png', frame)

    frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))
    cv2.imshow('Original Frame', frame)

    # wait for end key input
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

