import sys
sys.path.insert(0, '..')

import cv2
import time
import os
from src.util import img_processing as imgp
from src.util import cv_processing as cvp
from src.util import pil_processing as pilp
from PIL import Image, ImageFilter, ImageEnhance
from moviepy.editor import AudioFileClip, VideoFileClip

video_path = '../media/name.mp4'
target_vid_path = '../name_remastered.mp4'

audio = AudioFileClip(video_path)
target_vid = VideoFileClip(target_vid_path)

target_vid.audio = audio
target_vid.write_videofile(target_vid_path, codec='libx264', audio_codec='aac')

target_vid.close()
audio.close()
