"""
@Author: Ali Rihan
@Date: 08/03/2022
@Link: https://leetcode.com/problems/generate-parentheses/
"""


def generateParenthesis(self, n: int) -> List[str]:
      ans = []

      def generate(s, l, r):
          if len(s) == 2 * n:
              ans.append(s)
              return
          if l < n:
              generate(s + '(', l + 1, r)
          if r < l and r < n:
              generate(s + ')', l, r + 1)


      generate("", 0, 0)
      return ans
		
