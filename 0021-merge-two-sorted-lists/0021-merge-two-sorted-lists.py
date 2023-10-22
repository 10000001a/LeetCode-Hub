# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        pointer = None

        while list1 is not None and list2 is not None:
            if list2 is None or list1.val < list2.val:
                if result is None:
                    result = ListNode(list1.val)
                    pointer = result
                else:
                    pointer.next = ListNode(list1.val)
                    pointer = pointer.next

                list1 = list1.next


            elif list1 is None or list1.val >= list2.val:
                if result is None:
                    result = ListNode(list2.val)
                    pointer = result
                else:
                    pointer.next = ListNode(list2.val)
                    pointer = pointer.next

                list2 = list2.next


        
        if list1 is None and list2 is not None:
            if pointer is None:
                return list2
            pointer.next = list2

        if list2 is None and list1 is not None:
            if pointer is None:
                return list1
            pointer.next = list1
            
        return result