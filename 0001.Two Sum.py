"""
@Author: Ali Rihan
@Date: 12/09/2021
@Link: https://leetcode.com/problems/two-sum/
"""


def twoSum(self, nums: List[int], target: int) -> List[int]:
	nums_dict = {}
	for i in range(len(nums)):
		if (target - nums[i]) in nums_dict:
			return [nums_dict[target - nums[i]], i]
		nums_dict[nums[i]] = i
		
