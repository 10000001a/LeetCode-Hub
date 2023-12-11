import sys

In = sys.stdin.readline

OPERAND = 1000000007

def pow(x, y):
    if y == 1:
        return x

    tmp = pow(x, y // 2)

    if y % 2 == 1:
        return (tmp * tmp * x) % OPERAND

    return (tmp * tmp) % OPERAND


N, K = map(int, In()[:-1].split(' '))
K = min(K, N - K)

x = 1
y = 1
for i in range(1, K + 1):
    y *= i
    if y > OPERAND:
        y %= OPERAND

for j in range(N - K + 1, N + 1):
    x *= j
    if x > OPERAND:
        x %= OPERAND

print((x % OPERAND) * (pow(y, OPERAND - 2) % OPERAND) % OPERAND)
