"""
@Author: Ali Rihan
@Date: 27/01/2022
@Link: https://leetcode.com/problems/zigzag-conversion/
"""


def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr= [[] for i in range(numRows)]
        i = 0
        for c in range(len(s)):
            arr[i].append(s[c])
            if i == numRows - 1:
                down = False
            elif i == 0:
                down = True
            i += 1 if down else -1
        return "".join(list(map(lambda row: "".join(row), arr)))
