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

def render(algorithm):
  nums = generate_numbers()
  reset_colors()
  
  add_clip(nums)
  
  algorithm(nums)
  
  go_through(nums)

  if not os.path.exists(video_dir):
    os.mkdir(video_dir)

  final_clip = ImageSequenceClip(clips, fps=fps)

  final_clip.write_videofile(video_dir + 'movie.mp4', fps=fps)