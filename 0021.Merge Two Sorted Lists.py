"""
@Author: Ali Rihan
@Date: 04/01/2022
@Link: https://leetcode.com/problems/merge-two-sorted-lists/
"""


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if list1 is None:
          return list2
      if list2 is None:
          return list1

      if list1.val < list2.val:
          current_node = new_list = ListNode(list1.val)
          list1 = list1.next
      else:
          current_node = new_list = ListNode(list2.val)
          list2 = list2.next

      while list1 and list2:
          if list1.val < list2.val:
              current_node.next = ListNode(list1.val) 
              list1 = list1.next
          else:
              current_node.next = ListNode(list2.val)
              list2 = list2.next
          current_node = current_node.next

      while list1:
          current_node.next = ListNode(list1.val)
          list1 = list1.next
          current_node = current_node.next

      while list2:
          current_node.next = ListNode(list2.val)
          list2 = list2.next
          current_node = current_node.next

      return new_list
		
