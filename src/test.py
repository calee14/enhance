import cv2
import time
import os
from util import img_processing as imgp
from util import cv_processing as cvp
from util import pil_processing as pilp
from PIL import Image, ImageFilter, ImageEnhance

video_path = './media/name.mp4'

cap = cv2.VideoCapture(video_path)

cap.set(cv2.CAP_PROP_POS_FRAMES, 450)
success, frame = cap.read()

if success:

    img_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(img_array, 'RGB').convert('RGB')
    image.save('hi.png')
    
    # cv2.imwrite('bad.png', frame)
    
	# start image processing
    start = time.time()
    frame = cvp.default_process(frame)
    end = time.time()
    print("[INFO] image processing took {:.6f} seconds".format(
	end - start))

    # scale image to 4k
    frame = cv2.resize(frame, (frame.shape[1]*3, frame.shape[0]*3))
    
    # write images to file
    cv2.imwrite('original.png', frame)

    frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))
    cv2.imshow('Original Frame', frame)

    # wait for end key input
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

