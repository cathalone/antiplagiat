import math
import sys


def kronecker(matrix1: list, matrix2: list):
    return [[num1 * num2 for num1 in elem1 for num2 in matrix2[row]] for elem1 in matrix1 for row in
            range(len(matrix2))]


def identity(n: int):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def haar(n: int):
    if n % 2 == 1:
        n -= 1

    if n == 2:
        return [[0.707, 0.707], [0.707, -0.707]]

    return [[round(elem2 * 1 / math.sqrt(2), 3) for elem2 in elem1] for elem1 in kronecker(haar(n // 2), [[1, 1]]) +
            kronecker(identity(n // 2), [[1, -1]])]


# def hadamard(n):
#     if n == 2:
#         return [[1, 1], [1, -1]]
#     return kronecker(hadamard(n // 2), [[1, 1], [1, -1]])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        n = 5
    else:
        n = int(sys.argv[1])

    print(haar(n))
