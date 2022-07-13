"""
@Author: Ali Rihan
@Date: 03/02/2022
@Link: https://leetcode.com/problems/valid-parentheses/
"""


def isValid(self, s: str) -> bool:
      stack = []
      for p in s:
          if p in "({[":
              stack.append(p)
          else:
              if not stack:
                  return False
              if stack[-1] != '(' and p == ')':
                  return False
              if stack[-1] != '{' and p == '}':
                  return False
              if stack[-1] != '[' and p == ']':
                  return False
              stack.pop()
      if stack:
          return False
      return True
		
