import cv2
import time
import os
from util import img_processing as imgp
from util import cv_processing as cvp
from util import pil_processing as pilp

video_path = './media/name.mp4'

# init vid capture obj
cap = cv2.VideoCapture(video_path)
# video cap config
cap.set(cv2.CAP_PROP_POS_FRAMES, 400)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
vid_fps = cap.get(cv2.CAP_PROP_FPS)

# make vid writer with 4k frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)*3)
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)*3)
print('New video frame dim:', frame_width, frame_height)

out = cv2.VideoWriter('name_remastered.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width,frame_height), True)
# out = cv2.VideoWriter('name_remastered.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width,frame_height), True)


for i in range(60):
    print(f"Working on frame: {i+1}/{length}", end='\r')
    # read from video
    success, frame = cap.read()
    if success:
        
        frame = cv2.resize(frame, (frame.shape[1]*3, frame.shape[0]*3))
        # cv2.imshow('Frame', frame)

        # write new frame
        out.write(frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print("Prematurely stopped video processing because could not read next frame.")
        break

# display debrief
print(f"Working on frame: {i+1}/{length}")
print("Completed video processing.")
print(f"Processed {i+1}/{length} frames.")

# close lib programs
cap.release()
out.release()
cv2.destroyAllWindows()