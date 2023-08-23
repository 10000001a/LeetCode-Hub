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
        # target = n // 2 + n % 2
        print(start, end)
        target = (start + end) // 2 + (start + end) % 2
        guess_result = guess(target)
        print(guess_result)
        
        if guess_result == 0:
          return target
        
        if guess_result < 0:
          if target == end:
            end = target - 1
            continue
          
          end = target
        
        if guess_result > 0:
          if target == start:
            start = target + 1
            continue
          start = target
          
        
        