from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # self.maximum_list = [0 for _ in range(len(nums))]

        # m2 = nums[0]
        # m1 = nums[1]

        # max = nums[0]
        
        # maximum_list[0] = nums[0]
        # maximum_list[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     maximum_list[i] = max(maximum_list[i -1], maximum_list[i - 2] + nums[i])

        # return maximum_list[len(nums) - 1]

        @cache
        def memoization(index: int):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            
            return max(memoization(index - 1), memoization(index - 2) + nums[index])
        
        return memoization(len(nums) - 1)

        
        
        
