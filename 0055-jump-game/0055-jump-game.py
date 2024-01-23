class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cur_max = 0

        for i, n in enumerate(nums):
          if i <= cur_max:
            cur_max = max(cur_max, i + n)
          else:
            return False

        
        return True