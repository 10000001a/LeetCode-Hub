/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
  const letterCount = {};
  
  let result = 0;
  
  for (const x of s) {
    if (letterCount.hasOwnProperty(x)) {
      letterCount[x]++;
    } else {
      letterCount[x] = 1;
    }
  }
  

  let isContainOdd = false;
  
  for (const x in letterCount) {
    if (letterCount[x] % 2 === 1) {
      isContainOdd = true;
      result += letterCount[x] - 1;
    } else {
      result += letterCount[x];
    }
  }
  
  if (isContainOdd) return result + 1
  
  return result;
};