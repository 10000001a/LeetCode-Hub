import re

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'a|e|i|o|u|A|E|I|O|U';
        answer = ''
        
        # s가 가지고 있는 모음들을 역순으로 재배치합니다.
        consonants = re.split(vowels, s)
        reversed_vowels = re.findall(vowels, s)[::-1] + ['']
        
        for i in range(len(consonants)):
          answer += consonants[i]
          answer += reversed_vowels[i]
          
        return answer;
