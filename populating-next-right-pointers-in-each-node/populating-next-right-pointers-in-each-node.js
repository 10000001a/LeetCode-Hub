/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    if (root === null) return root;
    
    if (root.left !== null) {
        root.left.next = root.right;
        root.right.next = root.next !== null ? root.next.left : null
        connect(root.right)
        connect(root.left) 
    }
    return root;
};