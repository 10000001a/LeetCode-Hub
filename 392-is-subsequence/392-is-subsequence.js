/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
  if (t.length === 0) {
    if (s.length === 0) return true
    return false;  
  }
  
  let j = 0;
  
  for (let i = 0; i < t.length; i++) {
    if (t[i] === s[j]) {
      j++;
    }
    
    if (j === s.length) {
      return true;
    }
  }
  
  return false;
};