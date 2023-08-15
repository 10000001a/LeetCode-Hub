class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = 2 ** 31 - 1
        second_smallest = 2 ** 31
        target = 2 ** 31
        
        for i in nums:
          if i < smallest:
            smallest = i
            second_smallest = 2 ** 31;
          elif i < second_smallest and i > smallest:
            second_smallest = i
            target = min(target, second_smallest)
          
          if i > target:
            print(i)
            return True
        
        return False;
