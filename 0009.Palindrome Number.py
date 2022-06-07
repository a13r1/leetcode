"""
@Author: Ali Rihan
@Date: 13/12/2021
@Link: https://leetcode.com/problems/palindrome-number/
"""


def isPalindrome(self, x: int) -> bool:
      if x < 0:
          return False
      if x == 0:
          return True
      return x == int(str(x)[::-1])
		
