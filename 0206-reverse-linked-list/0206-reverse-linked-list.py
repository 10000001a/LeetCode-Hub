# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        reversedList = None

        while head is not None:
            reversedList = ListNode(head.val, reversedList)
            head = head.next

        return reversedList