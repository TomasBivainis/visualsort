from .module import *

def compare(a, b, nums):
  assign_color(a, "green")
  assign_color(b, "red")
  return nums[a] > nums[b]

def swap(a, b, nums):
  tmp = nums[a]
  nums[a] = nums[b]
  nums[b] = tmp
  add_clip(nums)
  reset_colors()
  return nums

def render(algorithm, video_directory = "./", vidoe_name = "movie", fps = 50):
  nums = generate_numbers()
  reset_colors()
  
  add_clip(nums)
  
  algorithm(nums)
  
  go_through(nums)

  if not os.path.exists(video_directory):
    os.mkdir(video_directory)

  final_clip = ImageSequenceClip(clips, fps=fps)

  final_clip.write_videofile(os.path.join(video_directory, vidoe_name + ".mp4"), fps=fps)