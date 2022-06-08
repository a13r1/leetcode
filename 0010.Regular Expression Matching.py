"""
@Author: Ali Rihan
@Date: 07/03/2022
@Link: https://leetcode.com/problems/regular-expression-matching/
"""


def isMatch(self, s: str, p: str) -> bool:
      cache = {}
      n = len(s)
      m = len(p)

      def dfs(i, j):
          if (i, j) in cache:
              return cache[(i, j)]
          if i >= n and j >= m:
              return True
          if j >= m:
              return False
          match = i < n and (s[i] == p[j] or p[j] == '.')
          if j + 1 < m and p[j + 1] == '*':
              cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
              return cache[(i, j)]
          if match:
              cache[(i, j)] = dfs(i + 1, j + 1)
              return cache[(i, j)]
          cache[(i, j)] = False
          return False

      return dfs(0, 0)
		
