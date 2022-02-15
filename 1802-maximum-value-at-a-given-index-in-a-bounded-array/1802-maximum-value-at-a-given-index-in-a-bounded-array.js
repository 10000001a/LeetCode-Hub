/**
 * @param {number} n
 * @param {number} index
 * @param {number} maxSum
 * @return {number}
 */
var maxValue = function(n, index, maxSum) {
  let result = 2;
  let head = index; tail = index;
  let sum = n + 1;
  
  while (sum <= maxSum) {
    if (head !== 0) head--;
    
    if (tail !== n - 1) tail++;
    
    result++;
    
    sum += (tail - head + 1);
    
    if (sum > maxSum) break;
  
    if (head === 0 && tail === n - 1) {
      const x = parseInt((maxSum - sum) / n);
      result += x;
      sum += x * n;
    }
  }
  
  return result - 1;
  
};