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
 * @return {number}
 */
var minDepth = function(root) {
  if (root === null) return 0;
  
  const queue = [{node: root, level: 1}];
  
  let answer = 100000;
  while (queue.length > 0) {
    const {node, level} = queue.shift();
    
    if (node.left === null && node.right === null && level < answer) {
      answer = level;
      continue;
    }
    
    if (node.left !== null) queue.push({node: node.left, level: level + 1});
    
    if (node.right !== null) queue.push({node: node.right, level: level + 1});
  }
  
  return answer;
};