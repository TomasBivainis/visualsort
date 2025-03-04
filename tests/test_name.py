import pytest
from unittest.mock import patch
from name import swap, compare

nums = [3, 2, 1]  

def test_swap():
  global nums
  
  with patch("name.add_clip"):
    with patch("name.reset_colors"):
      swap(0, 1, nums)
      assert nums == [2, 3, 1]
      
      swap(1, 2, nums)
      assert nums == [2, 1, 3]
  
def test_compare():
  global nums
  
  with patch("name.assign_color"):
    assert compare(0, 1, nums) == True
    assert compare(1, 0, nums) == False
    assert compare(0, 0, nums) == False
    