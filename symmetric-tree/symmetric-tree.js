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
 * @return {boolean}
 */
var isSymmetric = function(root) {
  if (root.left === null || root.right === null) {
    if (root.right === root.left) return true;
    return false;
  }
  
  if (root.left.val !== root.right.val) return false;
  
  const queueLeft = [root.left]
  const queueRight = [root.right]
  
  while (queueLeft.length !== 0 && queueRight.length !== 0) {
    const x = queueLeft.shift();
    
    const y = queueRight.shift();
    
    if (x === null || y === null) {
      if (x === y) continue;
      return false;
    }

    if (x.val === y.val) {
      queueLeft.push(x.left);
      queueLeft.push(x.right);
      
      queueRight.push(y.right);
      queueRight.push(y.left);
    } else return false;
  }
  
  if (queueLeft.length !== 0 && !queueLeft.every(item => item === null)) return false;
  if (queueRight.length !== 0 && !queueRight.every(item => item === null)) return false;
  
  return true;
};