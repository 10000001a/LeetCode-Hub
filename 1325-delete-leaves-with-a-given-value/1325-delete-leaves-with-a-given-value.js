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
 * @param {number} target
 * @return {TreeNode}
 */
var removeLeafNodes = function(root, target) {
  function dfs(node) {
    if (node === null) return null;
    
    const tn = new TreeNode(node.val);
   
    if (node.left !== null) {
      tn.left = dfs(node.left);
    }
    
    if (node.right !== null) {
      tn.right = dfs(node.right);
    }
    
    if (tn.val === target && tn.left === null && tn.right === null) {
      return null;
    }
    
    return tn;
     
  }
  
  return dfs(root);
};