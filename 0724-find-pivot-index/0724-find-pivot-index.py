class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
# nums의 총합을 구하기
# 총 합을 right라고 명칭하기
# 순회하며 원소 하나씩 왼쪽으로 넘기기

# 0 29
# 1 28
# 8 27
# 11 20
      left = 0
      # right = sum(nums) + nums[0]
      
      sum_nums = sum(nums)
      
      for index, num in enumerate(nums):
        left += num
        # right -= (nums[0] if index == 0 else nums[index - 1])
        # print(left, sum_nums - left + num)
        if left == sum_nums + num - left:
          return index
        
    
      return -1
        