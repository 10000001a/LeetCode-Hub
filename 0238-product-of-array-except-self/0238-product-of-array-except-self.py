class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
          return [0 for _ in range(len(nums))]
        
        all_multiplied = reduce(lambda x, y: (1 if x == 0 else x) * (1 if y == 0 else y), nums)
        
        if zero_count == 1:
          return [all_multiplied if i == 0 else 0 for i in nums]
        
        return [0 if i == 0 else all_multiplied // i for i in nums]