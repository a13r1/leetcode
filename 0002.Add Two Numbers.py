"""
@Author: Ali Rihan
@Date: 12/09/2021
@Link: https://leetcode.com/problems/add-two-numbers/
"""


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
	current_node = summation = ListNode()
	remainder = 0
	while True:
		s = l1.val + l2.val + remainder
		current_node.val = s % 10
		remainder = s // 10
		l1 = l1.next
		l2 = l2.next
		if not (l1 and l2):
			break
		current_node.next = ListNode()
		current_node = current_node.next
	while l1:
		current_node.next = ListNode()
		current_node = current_node.next
		s = l1.val + remainder
		current_node.val = s % 10
		remainder = s // 10
		l1 = l1.next
	while l2:
		current_node.next = ListNode()
		current_node = current_node.next
		s = l2.val + remainder
		current_node.val = s % 10
		remainder = s // 10
		l2 = l2.next  
	if remainder:
		current_node.next = ListNode(remainder)
	return summation
