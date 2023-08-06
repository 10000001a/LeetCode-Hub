class Solution:
    def longestPalindrome(self, s: str) -> str:
      longestStart = 0
      longestEnd = 0
      
      length = len(s)
      
      dp = [[i == j for i in range(length)] for j in range(length)]
      
      for i in range(1, length):
        x, y = 0, i
        
        while y < length:
          if y - x == 1:
            if s[x] == s[y]:
              dp[x][y] = True
              
              if longestEnd - longestStart < y - x:
                longestStart = x
                longestEnd = y
          else:
            if dp[x + 1][y - 1] and s[x] == s[y]:
              dp[x][y] = True
              
              if longestEnd - longestStart < y - x:
                longestStart = x
                longestEnd = y
          
          x += 1
          y += 1
          
      return s[longestStart:longestEnd + 1]
          

        
      