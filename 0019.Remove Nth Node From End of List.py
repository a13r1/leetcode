"""
@Author: Ali Rihan
@Date: 05/02/2022
@Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      stack = []
      curr = head
      while curr:
          stack.append(curr)
          curr = curr.next
      if n == len(stack):
          return stack[1] if n != 1 else None
      stack[-n - 1].next = stack[-n + 1] if n != 1 else None
      return head
		
