"""
@Author: Ali Rihan
@Date: 01/02/2022
@Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


def letterCombinations(self, digits: str) -> List[str]:
      if digits == "":
          return []

      digits_map = {
          '0': [''],
          '2': ['a', 'b', 'c'],
          '3': ['d', 'e', 'f'],
          '4': ['g', 'h', 'i'],
          '5': ['j', 'k', 'l'],
          '6': ['m', 'n', 'o'],
          '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'],
          '9': ['w', 'x', 'y', 'z']
      }
      digits = digits.zfill(4)
      result = []
      for c1 in digits_map[digits[0]]:
          for c2 in digits_map[digits[1]]:
              for c3 in digits_map[digits[2]]:
                  for c4 in digits_map[digits[3]]:
                      result.append(c1 + c2 + c3 + c4)
      return result
