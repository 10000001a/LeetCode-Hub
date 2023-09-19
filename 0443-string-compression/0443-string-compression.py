class Solution:
    def compress(self, chars: List[str]) -> int:
        char_list = []
        count_list = []

        count = 0
        for char in chars:
            if not char_list:
                char_list.append(char)
            else:
                if char == char_list[-1]:
                    pass
                else:
                    char_list.append(char)
                    count_list.append(count)
                    count = 0
            count += 1
        count_list.append(count)

        result = ''

        for i in range(len(char_list)):
            result = result + char_list[i]

            if count_list[i] == 1:
                continue

            for c in str(count_list[i]):
                result = result + c
        
        for (i, v) in enumerate(result):
            chars[i] = v

        return len(result)

        