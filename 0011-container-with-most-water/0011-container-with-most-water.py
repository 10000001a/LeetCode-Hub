class Solution:
    def maxArea(self, height: List[int]) -> int:
      start, end = 0, len(height) - 1
      
      result = (end - start) * min(height[start], height[end])
      
      while start <= end:
        result = max(result, (end - start) * min(height[start], height[end]))
        
        if height[start] < height[end]:
          start += 1
        else:
          end -= 1
          
      return result

      

          
          
          
        