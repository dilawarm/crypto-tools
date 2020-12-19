from square_and_multiply import square_and_multiply


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


def rsa(p, q, min_e, message):
    phi = (p - 1) * (q - 1)
    e = None
    for i in range(2, phi):
        gcd, _, _ = egcd(phi, i)
        if gcd == 1 and i > min_e:
            e = i
            break

    n = p * q
    print(f"Public key: {n, e}")

    _, x, _ = egcd(e, phi)
    d = x % phi

    print(f"Private key: {p, q, d}")

    enc_message = square_and_multiply(message, e, n, log=False)
    print(f"Encrypted message: {enc_message}")

    dec_message = square_and_multiply(enc_message, d, n, log=False)
    print(f"Decrypted message: {dec_message}")


if __name__ == "__main__":
    p = int(input("p: "))
    q = int(input("q: "))
    min_e = int(input("Minimum value for e: "))
    message = int(input("Message: "))

    rsa(p, q, min_e, message)