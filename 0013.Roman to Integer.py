"""
@Author: Ali Rihan
@Date: 31/01/2022
@Link: https://leetcode.com/problems/roman-to-integer/
"""


def romanToInt(self, s: str) -> int:
      rti = {
          "I": 1,
          "II": 2,
          "III": 3,
          "IV": 4,
          "V": 5,
          "IX": 9,
          "X": 10,
          "XL": 40,
          "L": 50,
          "XC": 90,
          "C": 100,
          "CD": 400,
          "D": 500,
          "CM": 900,
          "M": 1000
      }
      i = len(s) - 1
      num = 0
      while i >= 0:
          if i >= 2 and s[i - 2: i + 1] in rti:
              num += rti[s[i - 2: i + 1]]
              i -= 3
          elif i >= 1 and s[i - 1: i + 1] in rti:
              num += rti[s[i - 1: i + 1]]
              i -= 2
          else:
              num += rti[s[i]]
              i -= 1
      return num
      
