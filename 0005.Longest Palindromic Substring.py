"""
@Author: Ali Rihan
@Date: 21/01/2021
@Link: https://leetcode.com/problems/longest-palindromic-substring/
"""


def _getMaxPalindromeIndices(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r
                
    def longestPalindrome(self, s: str) -> str:
        min_l = max_r = 0
        for i in range(len(s)):
            odd_l, odd_r = self._getMaxPalindromeIndices(s, i, i)
            even_l, even_r = self._getMaxPalindromeIndices(s, i, i + 1)
            if max_r - min_l < odd_r - odd_l:
                min_l, max_r = odd_l, odd_r
            if max_r - min_l < even_r - even_l:
                min_l, max_r = even_l, even_r
        return s[min_l : max_r]
