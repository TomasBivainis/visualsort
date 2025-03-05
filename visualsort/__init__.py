from .module import *

def compare(a, b, nums):
  """
  Compares two numbers and updates the current frame.
  
  Args:
      a (int): The index of the first number in the array.
      b (int): The index of the second number in the array.
      nums (list): The array of numbers.

  Returns:
      bool: True if the first number is greater than the second number, False otherwise.

  Raises:
      IndexError: If either of the indices is out of bounds.
  """
  if(a < 0 or a >= len(nums) or b < 0 or b >= len(nums)):
    raise IndexError("Index out of bounds.")
  
  assign_color(a, "green")
  assign_color(b, "red")
  return nums[a] > nums[b]

def swap(a, b, nums):
  """
  Swaps two numbers and updates the current frame.

  Args:
      a (int): The index of the first number in the array.
      b (int): The index of the second number in the array.
      nums (list): The array of numbers.

  Returns:
      list: The array of numbers after the swap.

  Raises:
      IndexError: If either of the indices is out of bounds.
  """
  if(a < 0 or a >= len(nums) or b < 0 or b >= len(nums)):
    raise IndexError("Index out of bounds.")
  
  tmp = nums[a]
  nums[a] = nums[b]
  nums[b] = tmp
  add_clip(nums)
  reset_colors()
  return nums

def render(algorithm, video_directory = "./", vidoe_name = "movie", fps = 50):
  """
  Renders the given algorithm to a video.

  Args:
      algorithm (function): The sorting algorithm (writen using the provided visualsort functions) that will be rendered.
      video_directory (str): The dirrectory where the video file will be saved.
      video_name (str): The diseried name of the video file.
      fps (int): The frame rate of the video.

  Raises:
      IndexError: If either of the indices is out of bounds.
  """
  nums = generate_numbers()
  reset_colors()
  
  add_clip(nums)
  
  algorithm(nums)
  
  go_through(nums)

  if not os.path.exists(video_directory):
    os.mkdir(video_directory)

  final_clip = ImageSequenceClip(clips, fps=fps)

  final_clip.write_videofile(os.path.join(video_directory, vidoe_name + ".mp4"), fps=fps)