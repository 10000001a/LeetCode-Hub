import sys

IN = sys.stdin.readline

N = int(IN())

fibonacci_map = {
  0: 0,
  1: 1,
  2: 1,
  3: 2,
  4: 3,
}


def fibonacci(i: int) -> int:
  if i in fibonacci_map:
    return fibonacci_map[i]

  tmp = None
  if i % 2 == 0:  # 짝수
    tmp = fibonacci(i // 2) ** 2 + 2 * fibonacci(i // 2) * fibonacci(
        i // 2 - 1)
  else:  # 홀수
    tmp = fibonacci(i // 2 + 1) ** 2 + fibonacci(i // 2) ** 2

  if tmp >= 1000000:
    tmp %= 1000000

  fibonacci_map[i] = tmp

  return tmp


print(fibonacci(N))
