from dlp import shank
from rsa import egcd
from square_and_multiply import square_and_multiply


def elgamal(alpha, beta, p):
    print(f"Public Key: {p, alpha, beta}")
    a = shank(alpha, beta, p)
    print(f"Private Key: {a}")


def sign(message, k, alpha, p, a):
    _, a, _ = egcd(k, p - 1)
    x = a % (p - 1)

    y = square_and_multiply(alpha, k, p, log=False)

    return (y, ((message - alpha * y) * x) % (p - 1))


verify_signature = lambda message, signature, alpha, beta, p: square_and_multiply(
    beta, signature[0], p, log=False
) * square_and_multiply(
    signature[0], signature[1], p, log=False
) == square_and_multiply(
    alpha, message, p, log=False
)

if __name__ == "__main__":
    choice = input(
        """
    ElGamal [e]
    Sign message [s]
    Verify [v]
    """
    )
    p = int(input("p: "))
    alpha = int(input("alpha: "))
    beta = int(input("beta: "))
    a = int(input("a: "))
    if choice == "e":
        elgamal(alpha, beta, p)
    elif choice == "s":
        message = int(input("message: "))
        k = int(input("k: "))
        print(sign(message, k, alpha, p, a))
    else:
        message = int(input("message: "))
        signature = [int(x) for x in input("x,y: ").split(",")]
        print(verify_signature(message, signature, alpha, beta, p))