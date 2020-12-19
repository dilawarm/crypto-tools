import numpy as np
from square_and_multiply import square_and_multiply
from rsa import egcd

f = lambda x: x ** 2 + 1


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def pollard(n):
    k = 2
    while True:
        a = square_and_multiply(2, factorial(k), n, log=False)
        gcd, _, _ = egcd(a - 1, n)
        if gcd != 1:
            print(f"{n} = {gcd} x {n // gcd}, B = {k}")
            break
        k += 1


def pollard_rho(n):
    x, i = 1, 1
    while True:
        y = f(x)
        gcd, _, _ = egcd(y - x, n)
        if gcd != 1:
            print(f"{n} = {gcd} x {n // gcd}, Iterations = {i}")
            break
        x = y
        i += 1


if __name__ == "__main__":
    n = int(input("n: "))

    pollard(n)
    pollard_rho(n)