# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.

        Runtime
        89ms
        Beats 17.40%of users with Python3

        Memory
        16.22mb
        Beats 94.68%of users with Python3

        (결과로 알 수 있듯이 코드 수정 필요)
        링크드 리스트에서 값 읽기
        그 값을 반대로 출력
        """
        l_value  = ''
        while l1:
            l_value+=str(l1.val)
            l1=l1.next
        l1_value = int(l_value[::-1])

        l_value  = ''
        while l2:
            l_value+=str(l2.val)
            l2=l2.next
        l2_value = int(l_value[::-1])

        header=None
        linked_list=None
        for i in str(l1_value + l2_value):
            if not header:
                header=ListNode(int(i))
                linked_list=header
            else:
                curNode=ListNode(int(i),linked_list)
                linked_list=curNode
        
        return linked_list