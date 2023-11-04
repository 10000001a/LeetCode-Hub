class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0 for _ in range(len(temperatures))]

        max_num = [(0,0) for _ in range(len(temperatures))]
        max_num[-1] = (temperatures[-1], len(temperatures) - 1)

        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] < temperatures[i + 1]:
                result[i] = 1
                max_num[i] = (temperatures[i + 1], i + 1)
            else:
                maxi = max_num[i + 1][0]
                index = max_num[i + 1][1]

                if i + 1 == index:
                    print(i + 1)
                    result[i] = 0
                    max_num[i] = (temperatures[i], i)
                    continue

                while maxi <= temperatures[i] and result[index] != 0:
                    maxi = max_num[index][0]
                    index = max_num[index][1]

                if result[index] == 0 and temperatures[index] <= temperatures[i]:
                    result[i] = 0
                    max_num[i] = (temperatures[i], i)
                else:
                    result[i] = index - i
                    max_num[i] = (maxi, index)

        print(max_num)
        return result