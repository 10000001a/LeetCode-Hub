import sys

IN = sys.stdin.readline

N = int(IN())

mat_list = []
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
  r, c = map(int, IN()[:-1].split(' '))

  mat_list.append((r, c))

if N == 1:
  print(0)
  exit(0)

for x in range(1, N):
  for y in range(N - x):
    i, j = y, y + x

    candidate = []
    for d in range(0, j - i):
      candidate.append(
          mat_list[i][0] * mat_list[j][1] * mat_list[i + d][1] + \
          dp[i][i + d] + dp[i + d + 1][j])

    dp[i][j] = min(candidate)

print(dp[0][N - 1])
