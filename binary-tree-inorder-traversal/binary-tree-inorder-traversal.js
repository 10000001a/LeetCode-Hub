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
var inorderTraversal = function(root) {
  const result = [];
    
  // init
  const route = [];
  
  route.push(root);
  
  // run
  
  while(route.length > 0) {
    const pop = route.shift();
    
    if (pop === null) {
      
    } else if (typeof(pop) === 'number') {
      result.push(pop);
    } else {
      // const tmp = [pop.left, pop.val, pop.right];
      console.dir(pop)
      route.unshift(pop.left, pop.val, pop.right);
    }
  }

  return result;
};