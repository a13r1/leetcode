"""
@Author: Ali Rihan
@Date: 27/01/2022
@Link: https://leetcode.com/problems/reverse-integer/
"""


def reverse(self, x: int) -> int:
      x = -int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
      return x if -2**31 <= x <= 2**31 - 1 else 0
