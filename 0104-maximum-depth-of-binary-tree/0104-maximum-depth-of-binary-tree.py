from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    queue = deque([(root, 1)]);
    max_depth = 0
    while queue:
      node, depth = queue.popleft()
      if node:
        max_depth = max(max_depth, depth)
        left, right = node.left, node.right

        if left is not None:
          queue.append((left, depth + 1))
        if right is not None:
          queue.append((right, depth + 1))
      
    return max_depth;
      