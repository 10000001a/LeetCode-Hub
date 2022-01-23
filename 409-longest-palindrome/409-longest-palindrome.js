/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
  const letterCount = {};
  
  let result = 0;
  
  for (let i = 0; i < s.length; i++) {
    if (letterCount.hasOwnProperty(s[i])) {
      letterCount[s[i]]++;
    } else {
      letterCount[s[i]] = 1;
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