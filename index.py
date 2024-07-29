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
length = 50

column_width = video_width / length
column_height = ((video_height - header_height) / length)

duration = 0.2
fps = 15

nums = []
clips = []

video_dir = './video/'

for i in range(1, length + 1):
  nums.append(i)

random.shuffle(nums)

def make_frame():
  img = Image.new('RGB', (video_width, video_height))

  draw = ImageDraw.Draw(img)

  for i in range(len(nums)):
    draw.rectangle([(i * column_width, video_height - nums[i] * column_height), ((i + 1) * column_width, video_height)], (255, 255, 255))

  return asarray(img)

def add_clip():
  clips.append(make_frame())

for i in range(len(nums)):
  for j in range(i + 1, len(nums)):
    if nums[i] > nums[j]:
      tmp = nums[i]
      nums[i] = nums[j]
      nums[j] = tmp
      add_clip()

if not os.path.exists(video_dir):
  os.mkdir(video_dir)

final_clip = ImageSequenceClip(clips, fps=fps)

final_clip.write_videofile(video_dir + 'movie.mp4', fps=fps)