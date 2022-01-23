/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {  
  const getAmount = (s, e) => (e - s) * Math.min(height[e], height[s]);
  
  let start = 0, end = height.length - 1, amount = end * Math.min(height[0], height[end]);
  
  
  while (start < end) {
    amount = Math.max(getAmount(start, end), amount);
    
    if (height[start] > height[end]) end--;
    else start++;
  }
  
  return amount;
  
};