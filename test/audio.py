import sys
sys.path.insert(0, '..')

import cv2
import time
import os
from src.util import img_processing as imgp
from src.util import cv_processing as cvp
from src.util import pil_processing as pilp
from PIL import Image, ImageFilter, ImageEnhance
from moviepy import AudioFileClip, VideoFileClip

video_path = './media/name.mp4'

audio = AudioFileClip(video_path)
print(audio)

audio.close()
