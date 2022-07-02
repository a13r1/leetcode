"""
@Author: Ali Rihan
@Date: 04/02/2022
@Link: https://leetcode.com/problems/3sum-closest/
"""


def threeSumClosest(self, nums: List[int], target: int) -> int:
      nums.sort()
      min_diff = inf
      for i in range(len(nums) - 2):
          if i > 0 and nums[i - 1] == nums[i]:
              continue
          l = i + 1
          r = len(nums) - 1
          remaining = target - nums[i]
          while l < r:
              diff = abs(target - nums[i] - nums[l] - nums[r])
              if min_diff > diff:
                  min_diff = diff
                  closest_sum = nums[i] + nums[l] + nums[r]
              if nums[l] + nums[r] < remaining:
                  l += 1
              elif nums[l] + nums[r] > remaining:
                  r -= 1
              else:
                  while l < r and nums[l + 1] == nums[l]:
                      l += 1
                  l += 1
      return closest_sum
      
