/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) { 
  const queueP = [p];
  const queueQ = [q];
  
  while (queueP.length !== 0 && queueQ.length !== 0) {
    const visitingP = queueP.shift();
    const visitingQ = queueQ.shift();
    
    if (visitingP === null || visitingQ  === null) {
      if (visitingP === visitingQ) continue;
      
      return false;
    }
    
    if (visitingP.val === visitingQ.val) {
      queueP.push(visitingP.left);
      queueP.push(visitingP.right);
      
      queueQ.push(visitingQ.left);
      queueQ.push(visitingQ.right);
    } else {
      return false;    
    }
  }
  
  if (queueP.length > 0 && !queueP.every(item => item === null)) return false;
  if (queueQ.length > 0 && !queueQ.every(item => item === null)) return false;
  
  return true;
};