"""
@Author: Ali Rihan
@Date: 31/01/2022
@Link: https://leetcode.com/problems/longest-common-prefix/
"""


def longestCommonPrefix(self, strs: List[str]) -> str:
      lcp = ""
      curr = 0
      while curr < len(strs[0]):
          c = strs[0][curr]
          for i in range(len(strs)):
              if curr >= len(strs[i]) or strs[i][curr] != c:
                  return lcp
          lcp += c
          curr += 1
      return lcp
    
