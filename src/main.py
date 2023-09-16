import cv2
import time
import os
from util import cv_processing as cvp
import numpy as np
from moviepy.editor import AudioFileClip, VideoFileClip
import ffmpeg
from time import sleep

# define media paths
video_path = './media/name.mp4'
target_vid_path = './name_remastered.mp4'

# STATIC var for video quality
QUALITY_4k = 3
QUALITY_ULTRA_HD = 2
VID_QUALITY = 2

# init vid capture obj
cap = cv2.VideoCapture(video_path)
# video cap config
cap.set(cv2.CAP_PROP_POS_FRAMES, 400)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
vid_fps = cap.get(cv2.CAP_PROP_FPS)

# make vid writer with 4k frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)*VID_QUALITY)
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)*VID_QUALITY)
print('New video frame dim:', frame_width, frame_height)

out = cv2.VideoWriter(target_vid_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width,frame_height), True)
# out = cv2.VideoWriter('name_remastered.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width,frame_height), True)


for i in range(60):
    print(f"Working on frame: {i+1}/{length}", end='\r')
    # read from video
    success, frame = cap.read()
    if success:
        
        # process frame
        frame = cvp.default_process(frame)

        # scale image to ultra hd or 4k
        frame = cv2.resize(frame, (frame.shape[1]*VID_QUALITY, frame.shape[0]*VID_QUALITY))
        # cv2.imshow('Frame', frame)

        # compress image
        # enc = cv2.imencode('.png', frame, [cv2.IMWRITE_PNG_COMPRESSION, 8])[1]
        # enc = cv2.imencode('.jpp', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])[1]
        # frame = cv2.imdecode(enc, 1).astype(frame.dtype) 
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

# add audio to video
print(f"Start migration of audio file from {video_path} to {target_vid_path}.")

audio = AudioFileClip(video_path)
target_vid = VideoFileClip(target_vid_path)

target_vid.audio = audio
target_vid.write_videofile(target_vid_path, codec='libx264', audio_codec='aac', logger=None)

# display debrief
print(f"Completed migrating audio.")
# close lib programs
target_vid.close()
audio.close()

# compress video
bit_rate = '800k'
(
    ffmpeg
    .input('../name_remastered.mp4')
    .output('../name_remastered.mp4', b=bit_rate)
    .run()
)
