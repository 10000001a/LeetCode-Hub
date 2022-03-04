/**
 * @param {number[]} arr
 * @return {number}
 */
var subarrayBitwiseORs = function(arr) {
  let prev = new Set([]);
  let total = new Set(arr);
  
  
  for (let i = 0; i < arr.length; i++) {
    const curr = new Set([arr[i]]);
    
    for (const j of prev) {
      const tmp = j | arr[i];
      curr.add(tmp);
      total.add(tmp);
    }
    prev = curr;
  }
  
  return total.size;
};