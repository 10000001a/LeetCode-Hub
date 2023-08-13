# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#       (linked list의 길이) // 2에 해당하는 index의 노드를 제거하는 linked list를 반환)
      result = None
      val_list = linkedListToList(head)
      val_list.pop(getSize(head) // 2)
      
      for i in val_list[::-1]:
        result = ListNode(i, result)
      
      return result
  
def getSize(head: Optional[ListNode]):
    size = 0
    current = head

    while current:
      size += 1
      current = current.next

    return size;
  
def linkedListToList(head: Optional[ListNode]):
  l = []
  current = head

  while current:
    l.append(current.val)
    current = current.next
  
  return l