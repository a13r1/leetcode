"""
@Author: Ali Rihan
@Date: 31/01/2022
@Link: https://leetcode.com/problems/integer-to-roman/
"""


def intToRoman(self, num: int) -> str:
        s = num % 10
        num //= 10
        t = num % 10
        num //= 10
        h = num % 10
        num //= 10
        th = num % 10
        
        roman = []
        
        roman.append("M" * th)
        
        if h < 4:
            roman.append("C" * h)
        elif h == 4:
            roman.append("CD")
        elif 4 < h < 9:
            roman.append("D" + "C" * (h - 5))
        elif h == 9:
            roman.append("CM")
        
        if t < 4:
            roman.append("X" * t)
        elif t == 4:
            roman.append("XL")
        elif 4 < t < 9:
            roman.append("L" + "X" * (t - 5))
        elif t == 9:
            roman.append("XC")
            
        if s < 4:
            roman.append("I" * s)
        elif s == 4:
            roman.append("IV")
        elif 4 < s < 9:
            roman.append("V" + "I" * (s - 5))
        elif s == 9:
            roman.append("IX")
            
        return "".join(roman)
      
