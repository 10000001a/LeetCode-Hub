import sys

IN = sys.stdin.readline

N = int(IN()) % 1500000

fibonacci_map = []

i = -1
while i < N:
  i += 1
  if i == 0:
    fibonacci_map.append(0)
    continue
  if i == 1:
    fibonacci_map.append(1)
    continue

  v = fibonacci_map[i - 2] + fibonacci_map[i - 1]

  if v >= 1000000:
    v %= 1000000
  fibonacci_map.append(v)

print(fibonacci_map[N])
