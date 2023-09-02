# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target = head
        count = 0
        odd_start = None
        last = None

        while target:
            tmp = target.next

            if count == 1:
                odd_start = target
            
            if tmp is not None:
                target.next = target.next.next
            
            if count % 2 == 0:
                last = target
            
            target = tmp

            count = count + 1
        
        print(odd_start)
        print(head)

        print(target)
        print(last)
        if last is not None:
            last.next = odd_start

        return head
            
        #     target = target.next
        #     count = count + 1


        # # # even, odd = head, head.next if head is not None else None
        # even, odd = None, None
        # even_pointer, odd_pointer = None, None

        # count = 0
        # pointer = head

        # while pointer:
        #     if count % 2 == 0:
        #         if even is not None:
        #             even.next = pointer
        #             even = even.next
        #         else:
        #             even = pointer
        #             even_pointer = pointer
        #     else:
        #         if odd is not None:
        #             odd.next = pointer
        #             odd = odd.next
        #         else:
        #             odd = pointer
        #             odd_pointer = pointer

        #     count = count + 1
        #     pointer = pointer.next
        # print('a')
        # if even is not None:
        #     even.next = odd_pointer

        # print('b')
        # print(even_pointer)
        # print('c')
        # return even_pointer
