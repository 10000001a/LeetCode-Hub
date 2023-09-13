class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums 내림차순으로 정렬
        # k - 1번째 원소를 반환합니다.

        tmp = [0] * 20001
        count = 0

        for i in nums:
            tmp[i + 10000] = tmp[i + 10000] + 1
    
        
        for i, element in enumerate(reversed(tmp)):
            if count + element >= k:
                return (20000 - i) - 10000
            else:
                count = count + element
