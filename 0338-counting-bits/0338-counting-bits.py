class Solution:
    def countBits(self, n: int) -> List[int]:
#       0~n까지 각각 2진수로 변환 후 1의 갯수를 구한다.
#       0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000
#       0 1 1  2  1   2   2   3   1    2    2    3    2    3    3    4    1
        
        result = [0]
    
        for i in range(1, n + 1):
          half = i // 2
          r = i % 2
          
          result.append(result[half] + r)
          
        return result
          