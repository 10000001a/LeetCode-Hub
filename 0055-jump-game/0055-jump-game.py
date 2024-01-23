class Solution:
    def canJump(self, nums: List[int]) -> bool:
        new_nums = []
        
        for i, n in enumerate(nums):
            new_nums.append((i, i + n))
        
        cur_max = 0
        for tup in new_nums:
          if tup[0] <= cur_max:
            cur_max = max(cur_max, tup[1])
          else:
            return False
        
        return True