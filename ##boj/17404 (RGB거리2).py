import sys
from math import inf

In = sys.stdin.readline

N = int(In())


def init_resource_list():
    for i in range(N):
        r, g, b = map(int, In()[:-1].split(' '))
        resource_list.append([r, g, b])


def update_dp(color: int):
    x = dp[color]

    for i in range(2, N):
        if i == 2:
            x[i] = []

            for j in range(3):
                if j == color:
                    x[2].append(2001)
                else:
                    x[2].append(resource_list[2][j] + resource_list[1][color])
        else:
            x[i] = y(x, i)

    x[N] = []

    for i in range(3):
        if i == color:
            x[N].append(inf)
        else:
            tmp = list(map(lambda e: e[1], filter(lambda e: e[0] != i, enumerate(x[N - 1]))))
            x[N].append(resource_list[N][i] + min(tmp))


def y(dp: list, house_number: int) -> list:
    return [min(dp[house_number - 1][1], dp[house_number - 1][2]) + resource_list[house_number][0],
            min(dp[house_number - 1][0], dp[house_number - 1][2]) + resource_list[house_number][1],
            min(dp[house_number - 1][0], dp[house_number - 1][1]) + resource_list[house_number][2]]


resource_list = [[-1, -1, -1]]

init_resource_list()

dp = [[[0, 0, 0] for _ in range(N + 1)] for _ in range(3)]

for i in range(3):
    update_dp(i)


def get_min():
    return min(*list(dp[0][-1] + dp[1][-1] + dp[2][-1]))


print(get_min())
