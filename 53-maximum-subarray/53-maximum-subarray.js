/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  
  for (let i = 1; i < nums.length; i++) {
    nums[i] = Math.max(nums[i - 1] + nums[i], nums[i])
  }
  
  return Math.max(...nums);
};