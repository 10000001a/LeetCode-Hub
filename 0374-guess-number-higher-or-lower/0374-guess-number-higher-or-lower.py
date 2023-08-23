# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
      start = 1
      end = n

      while True:
        target = (start + end) // 2 + (start + end) % 2
        guess_result = guess(target)
        
        if guess_result == 0:
          return target
        
        if guess_result < 0:        
          end = target if target != end else target - 1
        
        if guess_result > 0:
          start = target if target != start else target + 1
          
        
        