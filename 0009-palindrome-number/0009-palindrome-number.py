class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_text = str(x)

        for i in range(len(x_text) // 2 + 1):
            print(x_text[i], x_text[-(i + 1)])
            if x_text[i] == x_text[-(i + 1)]:
                pass
            else: 
                return False
        
        return True