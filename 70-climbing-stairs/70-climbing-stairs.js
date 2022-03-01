/**
 * @param {number} n
 * @return {number}
 */
const x = {0: 0, 1: 1, 2: 2};
var climbStairs = function(n) {
  if (n === 1) return 1;
  if (n === 2) return 2;
  
  if (x[n]) return x[n];
  
  x[n] = climbStairs(n - 1) + climbStairs(n - 2);
  
  return x[n];
};