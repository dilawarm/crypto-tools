import numpy as np
from multiplicationtable import multiplicationTable


def multiplicative_inverse(n, m):
    y, x = 0, 1

    if m == 1:
        return 0

    while n > 1:
        q = n // m

        t = m

        m = n % m
        n, t = t, y

        y = x - q * y
        x = t

    return x


def inverse(K, m):
    det = int(np.linalg.det(K)) % m

    _, inverses, _ = multiplicationTable(m)
    if det not in inverses:
        print("Inverse does not exist")
        return

    return np.array(
        np.rint(
            (
                multiplicative_inverse(np.linalg.det(K), m)
                * np.linalg.det(K)
                * np.linalg.inv(K)
            )
            % m
        ),
        dtype=np.int,
    )


if __name__ == "__main__":
    n = int(input("Dimension of square matrix (integer): "))
    print(f"Row with {n} numbers:")
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    matrix = np.array(matrix, dtype=np.int)

    m = int(input("Modulo: "))
    print("Inverse matrix:")
    print(inverse(matrix, m))