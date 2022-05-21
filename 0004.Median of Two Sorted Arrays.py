"""
@Author: Ali Rihan
@Date: 02/04/2022
@Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            al = a[i] if i >= 0 else -inf
            ar = a[i + 1] if i + 1 < len(a) else inf
            bl = b[j] if j >= 0 else -inf
            br = b[j + 1] if j + 1 < len(b) else inf
            if al <= br and bl <= ar:
                if total % 2:
                    return min(ar, br)
                return (max(al, bl) + min(ar, br)) / 2
            if al > br:
                r = i - 1
            else:
                l = i + 1
