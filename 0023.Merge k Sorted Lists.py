"""
@Author: Ali Rihan
@Date: 05/02/2022
@Link: https://leetcode.com/problems/merge-k-sorted-lists/
"""


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      nums = []
      c = 0
      for node in lists:
          if node:
              c += 1
              heapq.heappush(nums, (node.val, c, node))
      head = curr = ListNode()
      while len(nums) > 0:
          curr.next = heapq.heappop(nums)[2]
          curr = curr.next
          if curr.next:
              c += 1
              heapq.heappush(nums, (curr.next.val, c, curr.next))
      return head.next
