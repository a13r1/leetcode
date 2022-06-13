"""
@Author: Ali Rihan
@Date: 16/01/2022
@Link: https://leetcode.com/problems/3sum/
"""


def threeSum(self, nums: List[int]) -> List[List[int]]:
      triplets = []
      if len(nums) < 3:
          return triplets
      nums.sort()
      for i in range(len(nums) - 2):
          if i > 0 and nums[i - 1] == nums[i]:
              continue
          l = i + 1
          r = len(nums) - 1
          remaining = -nums[i]
          while l < r:
              if nums[l] + nums[r] < remaining:
                  l += 1
              elif nums[l] + nums[r] > remaining:
                  r -= 1
              else:
                  triplets.append([nums[i], nums[l], nums[r]])
                  while l < r and nums[l + 1] == nums[l]:
                      l += 1
                  l += 1
      return triplets
      
