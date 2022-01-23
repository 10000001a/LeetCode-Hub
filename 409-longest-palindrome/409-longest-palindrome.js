/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
  const letterCount = {};
  
  let result = 0;
  
  for (const x of s) {
    letterCount[x] = (letterCount[x] || 0) + 1
    
    if (letterCount[x] % 2 === 0) {
      result += 2;
    }
  }
  
  return s.length > result ? result + 1 : result;
};