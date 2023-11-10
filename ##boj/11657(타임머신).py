import sys
from math import inf

In = sys.stdin.readline

N, M = map(int, In()[:-1].split(' '))

edges = []
# distance = []

for _ in range(M):
    a, b, c = map(int, In()[:-1].split(' '))
    edges.append((a, b, c))

distance_from_start = [inf] * (N + 1)


def x(start):
    distance_from_start[start] = 0

    for i in range(N):
        for (start_node, end_node, distance) in edges:
            if distance_from_start[start_node] == inf:
                continue

            if distance_from_start[start_node] + distance < distance_from_start[end_node]:
                distance_from_start[end_node] = distance_from_start[start_node] + distance

                if i == N - 1:
                    return True

    return False


if x(1):
    print(-1)
else:
    for i in distance_from_start[2:N + 1]:
        if i == inf:
            print(-1)
        else:
            print(i)
