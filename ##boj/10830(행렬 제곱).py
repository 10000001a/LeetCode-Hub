import sys

In = sys.stdin.readline


def mul_matrix(m: list[list[int]], n: list[list[int]]) -> list[list[int]]:
    new_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_matrix[i][j] = new_matrix[i][j] + (m[i][k] * n[k][j])

            new_matrix[i][j] = new_matrix[i][j] % 1000 if new_matrix[i][j] >= 1000 else new_matrix[i][j]

    return new_matrix


def square_matrix(m: list[list[int]]) -> list[list[int]]:
    new_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_matrix[i][j] = new_matrix[i][j] + (m[i][k] * m[k][j])

            new_matrix[i][j] = new_matrix[i][j] % 1000 if new_matrix[i][j] >= 1000 else new_matrix[i][j]

    return new_matrix


N, B = map(int, In()[:-1].split(' '))

matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(lambda x: int(x) if int(x) < 1000 else 0, In()[:-1].split(' ')))

# matrix_square_list[index] = 주어진 행렬 ^ index
matrix_square_list = [0, matrix]

binary_b = format(B, 'b')

for t in range(1, len(binary_b)):
    matrix_square_list.append(square_matrix(matrix_square_list[t]))

result = None
start = len(binary_b)
for binary in str(binary_b):
    if binary == '1':
        if result is None:
            result = matrix_square_list[start]
        else:
            result = mul_matrix(result, matrix_square_list[start])

    start = start - 1

for i in range(N):
    print(" ".join(map(str, result[i])))
