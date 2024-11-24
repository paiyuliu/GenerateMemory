import glob
from moviepy.editor import *
import datetime

# 加載圖片和音樂
# 替換成你的圖片文件名
# image_files = ["BOY_8915.JPG", "BOY_8916.JPG", "BOY_8917.JPG"]
image_files = glob.glob("./Images/BOY*.jpg")
# 替換成你的 MP3 文件名
audio_file = "Haunting_Dark_Jazz.mp3"  

# 建立圖片剪輯 每張圖片顯示5秒
clips = [ImageClip(img).set_duration(4).crossfadein(1).crossfadeout(1) for img in image_files]
video = concatenate_videoclips(clips, method="compose")

# 添加音樂
audio = AudioFileClip(audio_file)
video = video.set_audio(audio)

# 添加效果（例如淡入淡出）
video = video.fadein(1).fadeout(1).crossfadein(1).crossfadeout(1)

# 保存影片
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#video.write_videofile(f"output_{current_time}.mp4", fps=5)
video.write_videofile(f"output_{current_time}.mp4", fps=5, codec="libx264", threads=8, preset="ultrafast")
