class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        head = 0
        tail = len(nums) - 1

        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        while head < tail:
            print(head, tail)
            half = (head + tail) // 2

            if half == 0:
                if nums[half] > nums[1]:
                    return half
            
            if half == len(nums) - 1:
                if nums[half] > nums[half - 1]:
                    return half
            
            if nums[half] > nums[half - 1] and nums[half] > nums[half + 1]:
                return half
            
            if nums[half] < nums[half - 1]:
                tail = half
                continue
            
            if nums[half] < nums[half + 1]:
                head = half
                continue
        
        return tail
            
