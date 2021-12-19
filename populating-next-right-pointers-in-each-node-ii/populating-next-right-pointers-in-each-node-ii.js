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
        if (root.right !== null) {
            root.left.next = root.right;
        }
        
        if (root.right === null) {
            let tmp = root.next;
            while (tmp !== null) {
                if (tmp.left) {
                    root.left.next = tmp.left;
                    break;
                }
                if (tmp.right) {
                    root.left.next = tmp.right;
                    break;
                }
                
                tmp = tmp.next;
            }
        }
    }
    
    
    if (root.right !== null) {
        let tmp = root.next;
        while (tmp !== null) {
            if (tmp.left) {
                root.right.next = tmp.left;
                break;
            }
            if (tmp.right) {
                root.right.next = tmp.right;
                break;
            }
            tmp = tmp.next;
        }
    }

    if (root.right === null && root.left === null) {
        return root;
    }
    
    if (root.right) connect(root.right);
    if (root.left) connect(root.left);
    
    
    return root
};