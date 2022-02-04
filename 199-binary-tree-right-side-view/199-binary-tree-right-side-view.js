/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
  const result = {};
  
  function bfs(node, i = 0) {
    if (!node) return;
    
    result[i] = node.val;
    
    if (node.left) bfs(node.left, i + 1);
    
    if (node.right) bfs(node.right, i + 1);
  }
  
  bfs(root);
  
  
  return Object.values(result);
};