import sys
from math import inf

In = sys.stdin.readline

V, M = map(int, In()[:-1].split(' '))

distance_map = [[inf for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(M):
    a, b, c = map(int, In()[:-1].split(' '))
    distance_map[a][b] = c

for i in range(1, V + 1):
    range2 = list(range(1, i)) + list(range(i + 1, V + 1))

    for j in range2:
        for k in range2:
            distance_map[j][k] = min(distance_map[j][k], distance_map[j][i] + distance_map[i][k])

result = inf
for i in range(1, V + 1):
    result = min(result, distance_map[i][i])
#
# for d in distance_map:
#     print(d)

if result == inf:
    print(-1)
else:
    print(result)
