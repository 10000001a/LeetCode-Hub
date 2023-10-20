class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        print(s.count('m'))

        thousand = 0
        hundred = 0
        ten = 0
        one = 0

        for i in s:
            if i == 'M':
                hundred = -hundred
                thousand += 1
            if i == 'D':
                hundred = -hundred + 5
            if i == 'C':
                ten = -ten
                hundred = hundred + 1
            if i == 'L':
                ten = -ten + 5
            if i == 'X':
                one = -one
                ten = ten + 1
            if i == 'V':
                one = -one + 5
            if i == 'I':
                one = one + 1

        return thousand * 1000 + hundred * 100 + ten * 10 + one        