class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = 0
        sum_ = 0

        for i in gain:
            sum_ = sum_ + i
            max_ = max(sum_, max_)

        return max_
        