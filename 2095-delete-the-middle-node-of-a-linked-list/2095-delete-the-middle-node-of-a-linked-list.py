# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#       (linked list의 길이) // 2에 해당하는 index의 노드를 제거하는 linked list를 반환)
#  size 구하기
#  target 구하기
#  head를 순회할 때, index를 확인하기
#  index == target -1 
#  해당 노드의 next를 다다음 노드로 꽂아주기

    size = getSize(head)
    target = size // 2
  
    x = None
    for i in range(target):
      if x is None:
        x = head
      else:
        x = x.next
    if x is not None:
      x.next = x.next.next
      return head
    else:
      return None
    
def getSize(head: Optional[ListNode]):
    size = 0
    current = head

    while current:
      size += 1
      current = current.next

    return size;