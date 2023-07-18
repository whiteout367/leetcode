from typing import Optional

"""
linked list 공부 필요
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        head = current = ListNode(0)

        while node1 and node2:

            if node1.val < node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next

            current = current.next

        if node1:
            current.next = node1
        elif node2:
            current.next = node2

        return head.next