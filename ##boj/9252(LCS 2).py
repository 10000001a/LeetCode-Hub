import sys

In = sys.stdin.readline

first_string = In()[:-1]
second_string = In()[:-1]

first_string_length = len(first_string)
second_string_length = len(second_string)

dp = [[0 for _ in range(first_string_length + 1)] for _ in range(second_string_length + 1)]

for i in range(1, second_string_length + 1):
    for j in range(1, first_string_length + 1):
        # if second_string[i - 1] == first_string[j - 1] and dp[i - 1][j] == dp[i][j - 1]:
        if second_string[i - 1] == first_string[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[second_string_length][first_string_length])

result = ""

x = second_string_length
y = first_string_length
while x > 0 and y > 0:
    if dp[x - 1][y] > dp[x][y - 1] or dp[x - 1][y] == dp[x][y]:
        x = x - 1
    elif dp[x - 1][y] < dp[x][y - 1] or dp[x][y - 1] == dp[x][y]:
        y = y - 1
    else:
        result = second_string[x - 1] + result
        x = x - 1
        y = y - 1

if len(result) > 0:
    print(result)
