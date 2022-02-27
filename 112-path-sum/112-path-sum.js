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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
  function dfs({val, left, right}) {
    let leftBool = false, rightBool = false;
    
    if (left !== null) {
      left.val += val;
      
      leftBool = dfs(left);
    }
    
    if (right !== null) {
      right.val += val;
      
      rightBool = dfs(right);
    }
    
    if (right === null && left === null && val === targetSum) {
      return true;
    }
    
    
    return leftBool || rightBool;
  }
  
  if (!root) return false;
  
  return dfs(root);
};