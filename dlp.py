import math
from square_and_multiply import square_and_multiply
from rsa import egcd


def shank(alpha, beta, p):
    k = math.ceil(math.sqrt(p))
    print(f"m = {k}")
    alpha_k = square_and_multiply(alpha, k, p, log=False)
    print(f"alpha^m = {alpha_k}")
    alpha_ks = [square_and_multiply(alpha_k, j, p, log=False) for j in range(k)]
    print(alpha_ks)

    _, x, _ = egcd(alpha, p)
    alpha_inverse = x % p

    beta_alpha_inverse = 0
    print(f"Mult. invers: {alpha_inverse}")

    a, b = 0, 0
    for i in range(k):
        beta_alpha_inverse = (
            beta * square_and_multiply(alpha_inverse, i, p, log=False)
        ) % p
        print(beta_alpha_inverse)
        found = False
        for j in range(k):
            if alpha_ks[j] == beta_alpha_inverse:
                a, b = j, i
                found = True
                break
        if found:
            break

    return a * k + b


if __name__ == "__main__":
    p = int(input("p: "))
    alpha = int(input("alpha: "))
    beta = int(input("beta: "))

    print(shank(alpha, beta, p))