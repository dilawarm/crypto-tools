def square_and_multiply(a, b, n, log=True):
    b = bin(b)[2:]
    z = 1
    for i in range(len(b)):
        if log:
            print(f"{b[i]}: ", end="")
        if b[i] == "1":
            y = ((z ** 2) * a) % n
            if log:
                print(f"z = {z}^2 * {a} = {y}")
            z = y
        else:
            y = (z ** 2) % n
            if log:
                print(f"z = {z}^2 = {y}")
            z = y
    return z


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    n = int(input("n: "))

    square_and_multiply(a, b, n)
