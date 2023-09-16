from moviepy.editor import AudioFileClip, VideoFileClip, VideoClip, AudioClip, CompositeAudioClip
import numpy as np

# define media paths
video_path = './media/name.mp4'
target_vid_path = './name_remastered - Copy.mp4'

# add audio to video
print(f"Start migration of audio file from {video_path} to {target_vid_path}.")

# audio = VideoFileClip(video_path).audio
# audio.write_audiofile('name_audio.mp3')

audio = AudioFileClip('name_audio.mp3')
video = VideoFileClip(target_vid_path)

new_audioclip = CompositeAudioClip([audio])
video = video.set_audio(new_audioclip)

video.write_videofile('newvid.mp4', fps=30, audio_codec='aac')

# display debrief
print(f"Completed migrating audio.")

# close lib programs
audio.close()
video.close()