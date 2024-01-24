class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_spend_hour(candidate_k):
            return sum(map(lambda b: b // candidate_k if b % candidate_k == 0 else b // candidate_k + 1, piles))

        min_k = 1
        max_k = max(piles)
        print('')
        candidate = (max_k + min_k) // 2
        
        while min_k < max_k:
            if candidate == 0:
                break
            spend_hour = get_spend_hour(candidate)
            print(candidate, spend_hour)
            print(min_k, max_k)
            print(' ')

            if spend_hour > h:
                min_k = candidate + 1
                # candidate 업데이트
            
            if spend_hour <= h:
                max_k = candidate 
            
            candidate = (max_k + min_k) // 2
            

        
        return candidate