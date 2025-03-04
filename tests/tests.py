import unittest
from unittest.mock import patch
from name import swap, compare

class TestName(unittest.TestCase):
  nums = []

  def setUp(self):
    global nums
    nums = [3, 2, 1]

  @patch("name.add_clip")
  @patch("name.reset_colors")
  def test_swap(self, mock_add_clip, mock_reset_colors):
    global nums
    
    swap(0, 1, nums)
    self.assertEqual(nums, [2, 3, 1])
    
    swap(1, 2, nums)
    self.assertEqual(nums, [2, 1, 3])
    
  @patch("name.assign_color")
  def test_compare(self, mock_assign_color):
    global nums
    
    self.assertTrue(compare(0, 1, nums))
    self.assertFalse(compare(1, 0, nums))
    self.assertFalse(compare(0, 0, nums))
    
if __name__ == "__main__":
  unittest.main()
    