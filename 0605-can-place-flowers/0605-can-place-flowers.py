class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        answer = 0
        emptyCount = [0]

        for i in [0, *flowerbed, 0]:
            if (i):
                emptyCount.append(0)
            else:
                emptyCount[-1] += 1

        for j in emptyCount:
            answer += (0 if j == 0 else (j - 1) // 2)

            if (answer >= n):
                return True

        return False