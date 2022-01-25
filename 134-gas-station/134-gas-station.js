/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
  let sum = 0, result = 0, total = 0;
  
  for (let i = 0; i < gas.length; i++) {
    const margin = gas[i] - cost[i];
    
    total += margin
    if (sum + margin < 0) {
      result = i + 1;
      sum = 0;
      continue;
    } else {
      sum += margin;
    }
  }
  
  if (total < 0) return -1;
  
  return result;
};