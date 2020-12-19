from square_and_multiply import square_and_multiply
import pandas as pd
import numpy as np


def find_orders(n):
    orders = {}
    table = []
    for i in range(1, n):
        row = []
        found = False
        for j in range(1, n):
            val = square_and_multiply(i, j, n, log=False)
            row.append(val)
            if val == 1 and not found:
                orders[i] = j
                found = True
        table.append(row)
    return orders, table


def logarithm_table(n):
    _, order_table = find_orders(n)
    table = []
    for i in range(1, n):
        row = []
        for j in range(1, n):
            found = False
            for k in range(len(order_table[i - 1])):
                if order_table[i - 1][k] == j:
                    found = True
                    row.append(k + 1)
                    break
            if not found:
                row.append(0)
        table.append(row)
    table = pd.DataFrame(table, dtype="int")
    table.index = np.arange(1, len(table) + 1)
    table.columns = np.arange(1, len(table) + 1)
    return table


if __name__ == "__main__":
    n = int(input("n: "))
    orders, _ = find_orders(n)
    print(f"Orders of all elements in Z_{n}: {orders}")
    print("Logarithm table: ")
    print(logarithm_table(n))