def euclidean_algorithm(a, b, log=True):
    x, y = a, b
    while True:
        q, r = a // b, a % b
        if log:
            print(f"{a} = {b} * {q} + {r}")
        if r == 0:
            break
        a, b = b, r
    if log:
        print(f"gcd({x}, {y}) = {b}")
    return b


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))

    if a > b:
        euclidean_algorithm(a, b)
    else:
        euclidean_algorithm(b, a)