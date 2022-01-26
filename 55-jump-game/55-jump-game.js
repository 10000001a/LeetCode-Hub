/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
  let max = 0;  
  
  for (let i = 0; i < nums.length; i++) {
    const maxJump = i + nums[i];
    
    if (i > max) return false;
    
    if (maxJump > max) max = maxJump;
  }
  
  return true;
};