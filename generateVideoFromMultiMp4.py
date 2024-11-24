# concat /Images/*mp4 to /output.mp4
# Usage: python generateVideoFromMultiMp4.py
import glob
import os
from moviepy.editor import *
import datetime

# 加載圖片和音樂
# 替換成你的圖片文件
mp4_files = glob.glob("./Images/*.mp4")
# 替換成你的 MP3 文件名
audio_file = "Haunting_Dark_Jazz.mp3"

# generate a list of video clips from mp4 files
clips = [VideoFileClip(mp4).fadein(1).fadeout(1) for mp4 in mp4_files]
video = concatenate_videoclips(clips, method="compose")

# 添加音樂
audio = AudioFileClip(audio_file)
video = video.set_audio(audio)

# 添加效果（例如淡入淡出）
video = video.fadein(1).fadeout(1).crossfadein(1).crossfadeout(1)

# 保存影片
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
video.write_videofile(f"output_{current_time}.mp4", fps=5)
