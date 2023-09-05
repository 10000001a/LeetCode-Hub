class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        count_star = 0
        
        for i in s[::-1]:
            if i == '*':
                count_star += 1
            else:
                if count_star > 0:
                    count_star -= 1
                else:
                    result.insert(0, i)
        

        return ''.join(result)

        