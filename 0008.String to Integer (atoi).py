"""
@Author: Ali Rihan
@Date: 29/01/2022
@Link: https://leetcode.com/problems/string-to-integer-atoi/
"""


def myAtoi(self, s: str) -> int:
      i = 0
      while i < len(s) and s[i] == ' ':
          i += 1
      sign = 1
      if i < len(s) and s[i] == '-':
          sign = -1
          i += 1
      elif i < len(s) and s[i] == '+':
          i += 1
      num = 0
      while i < len(s) and '0' <= s[i] <= '9':
          num *= 10
          num += ord(s[i]) - ord('0')
          i += 1
      num *= sign
      if num < -2**31:
          return -2**31
      if num > 2**31 - 1:
          return 2**31 - 1
      return num
