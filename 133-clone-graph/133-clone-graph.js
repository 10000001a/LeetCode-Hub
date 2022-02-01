/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
  const visited = {}
  
  const dfs = (node) => {
    if (!node) return node;
    
    if (visited[node.val]) return visited[node.val];
    
    const root = new Node(node.val);
    
    visited[node.val] = root;
    
    // root.neighbors = node.neighbors.map(n => dfs(n));
    node.neighbors.forEach(n => root.neighbors.push(dfs(n)))
    
    return root;
  }
  
  return dfs(node);
};