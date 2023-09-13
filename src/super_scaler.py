import cv2
import time
import os
from util import img_processing as imgp
from util import cv_processing as cvp
from util import pil_processing as pilp

video_path = './media/name.mp4'
model = './models/ESPCN_x4.pb'
# parse model metadata
modelName = model.split('/')[-1].split("_")[0].lower()
modelScale = model.split("_x")[-1]
modelScale = int(modelScale[:modelScale.find(".")])

cap = cv2.VideoCapture(video_path)
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(model)
sr.setModel(modelName, modelScale)

cap.set(cv2.CAP_PROP_POS_FRAMES, 400)
success, frame = cap.read()
if success:
    # use the super resolution model to upscale the image, timing how
    # long it takes
    small_frame = cv2.resize(frame, (int(frame.shape[1]//(2)), int(frame.shape[0]//(2))))
    frame = cv2.resize(frame, (frame.shape[1]*4, frame.shape[0]*4))
    cv2.imwrite('bad.png', frame)
    # start processing
    start = time.time()
    upscaled = sr.upsample(small_frame)
    processed = cvp.default_process(upscaled)
    frame = cvp.default_process(frame)
    end = time.time()
    print("[INFO] super resolution took {:.6f} seconds".format(
	end - start))
    
    # write images to file
    cv2.imwrite('test.png', processed)
    cv2.imwrite('original1.png', frame)

    processed = cv2.resize(processed, (int(processed.shape[1]*0.75), int(processed.shape[0]*0.75)))
    cv2.imshow('Upscaled Frame', processed)
    frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))
    cv2.imshow('Original Frame', frame)

    # wait for end key input
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

# while True:
#     success, frame = cap.read()
#     if success:
#         cv2.imshow('Frame', frame)

#         # Press Q on keyboard to  exit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#         break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()