import sys

In = sys.stdin.readline

T = int(In())

for _ in range(T):
  K = int(In()[:-1])
  fileSize = list(map(int, In()[:-1].split(' ')))
  dp = [[1e9] * K for _ in range(K)]

  subsum = [0] * K
  subsum[0] = fileSize[0]
  dp[0][0] = 0
  for i in range(1, K):
    subsum[i] = subsum[i - 1] + fileSize[i]
    dp[i][i] = 0

  for d in range(1, K):
    for i in range(K - d):
      for j in range(d):
        dp[i][i + d] = min(dp[i][i + d],
                           dp[i][i + j] +
                           dp[i + j + 1][
                             i + d] + (
                               subsum[i + d] - (
                             subsum[
                               i - 1] if i - 1 >= 0 else 0)))

  print(dp[0][K - 1])
