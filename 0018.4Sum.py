"""
@Author: Ali Rihan
@Date: 04/02/2022
@Link: https://leetcode.com/problems/4sum/
"""


def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
      nums.sort()
      n = len(nums)
      quads = set()
      for i in range(n - 1):
          for j in range(i + 1, n):
              curr_target = target - nums[i] - nums[j]
              l, r = j + 1, n - 1
              while l < r:
                  if nums[l] + nums[r] < curr_target:
                      l += 1
                  elif nums[l] + nums[r] > curr_target:
                      r -= 1
                  else:
                      quads.add((nums[i], nums[j], nums[l], nums[r]))
                      l += 1
                      r -= 1
      return quads
		
