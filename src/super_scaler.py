import cv2
import time
import os
from .util import img_processing

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

cap.set(cv2.CAP_PROP_POS_FRAMES, 250)
success, frame = cap.read()
if success:
    # use the super resolution model to upscale the image, timing how
    # long it takes
    small_frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))
    start = time.time()
    upscaled = sr.upsample(small_frame)
    end = time.time()
    print("[INFO] super resolution took {:.6f} seconds".format(
	end - start))
    frame = cv2.resize(frame, (frame.shape[1]*2, frame.shape[0]*2))
    cv2.imshow('Upscaled Frame', upscaled)
    cv2.imshow('Original Frame', frame)
    k = cv2.waitKey(10000)

    if k == 27:         # If escape was pressed exit
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