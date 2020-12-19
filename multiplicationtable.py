import pandas as pd
import numpy as np


def multiplicationTable(n):
    mult_inverses = []
    mult_inverse = []
    m = np.zeros((n, n))
    for i in range(1, n):
        for j in range(1, n):
            m[i][j] = (i * j) % n
            if m[i][j] == 1:
                mult_inverses.append((i, j))
                mult_inverse.append(i)
    m = pd.DataFrame(m, dtype="int")
    m = m.drop([0])
    m = m.drop([0], axis=1)
    return m, mult_inverse, mult_inverses


if __name__ == "__main__":
    n = int(input("n: "))

    m, _, mult_inverses = multiplicationTable(n)
    print(m)
    print()
    print(f"Multiplicative inverses mod {n}: {mult_inverses}")