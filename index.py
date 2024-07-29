from PIL import Image, ImageDraw
import random
import os
from numpy import asarray
os.environ["IMAGEIO_FFMPEG_EXE"] = "./ffmpeg"
from moviepy.editor import *
os.environ["IMAGEIO_FFMPEG_EXE"] = "./ffmpeg"

video_width = 1280
video_height = 720
header_height = 40
length = 20

column_width = video_width / length
column_height = ((video_height - header_height) / length)

duration = 0.2
fps = 15

nums = []

for i in range(1, length + 1):
  nums.append(i)
  
random.shuffle(nums)

img_dir = './current_images/'
clips = []

def make_frame(t):
  img = Image.new('RGB', (video_width, video_height))

  draw = ImageDraw.Draw(img)

  for i in range(len(nums)):
    draw.rectangle([(i * column_width, video_height - nums[i] * column_height), ((i + 1) * column_width, video_height)], (255, 255, 255))
  
  return asarray(img)

def add_clip():
  with VideoClip(make_frame, duration=duration) as clip:
    clip.write_videofile('tmp.mp4', fps=fps)
    new_clip = VideoFileClip('tmp.mp4')
    clips.append(new_clip)
    os.remove('tmp.mp4')

for i in range(len(nums)):
  for j in range(i + 1, len(nums)):
    if nums[i] > nums[j]:
      tmp = nums[i]
      nums[i] = nums[j]
      nums[j] = tmp
      add_clip()

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile('movie.mp4', fps=fps)

for file in os.listdir(img_dir):
  print(file)