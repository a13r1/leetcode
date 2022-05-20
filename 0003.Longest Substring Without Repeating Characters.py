"""
@Author: Ali Rihan
@Date: 12/10/2021
@Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def lengthOfLongestSubstring(self, s: str) -> int:
    max_length = 0
    distinct_chars = dict()
    i = j = 0
    for j in range(len(s)):
        char = s[j]
        if char in distinct_chars:
            if i <= distinct_chars[char]:
                i = distinct_chars[char] + 1
        distinct_chars[char] = j
        max_length = max(max_length, j - i + 1)
    return max_length
  
