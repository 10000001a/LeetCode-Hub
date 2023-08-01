# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0

    
    queue = [root];
    depth = 0;
    
    while queue:
      length = len(queue)
      
      for i in range(length):
        left, right = queue[i].left, queue[i].right
        
        if queue[i].left is not None:
          queue.append(queue[i].left)
        if queue[i].right is not None:
          queue.append(queue[i].right)
      
      queue = queue[length:]
      
      depth += 1
    
    return depth;
      