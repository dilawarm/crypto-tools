import numpy as np
import operator
import string
from inversematrix import inverse

ALPHABET = string.ascii_uppercase + "ÆØÅ"


def hill_cipher(plaintext, K, algo):
    K = K if algo.lower() == "encrypt" else inverse(K, len(ALPHABET))
    return "".join(
        part
        for part in [
            "".join(ALPHABET[int(mult[i]) % len(ALPHABET)] for i in range(len(mult)))
            for mult in [
                np.dot(
                    np.array(
                        [ALPHABET.index(part[i].upper()) for i in range(len(part))]
                    ),
                    K,
                )
                for part in [
                    plaintext[i : i + K.shape[0]]
                    for i in range(0, len(plaintext), K.shape[0])
                ]
            ]
        ]
    )


def findK(plaintext, enc_message, m):
    return (
        np.dot(
            np.array(
                [
                    [ALPHABET.index(part[i].upper()) for i in range(len(part))]
                    for part in [
                        enc_message[i : i + m] for i in range(0, len(enc_message), m)
                    ]
                ]
            ).T,
            inverse(
                np.array(
                    [
                        [ALPHABET.index(part[i].upper()) for i in range(len(part))]
                        for part in [
                            plaintext[i : i + m] for i in range(0, len(plaintext), m)
                        ]
                    ]
                ).T,
                len(ALPHABET),
            ),
        ).T
        % len(ALPHABET)
    )


def makeKey():
    print("Key:")
    n = int(input("Dimension of square matrix (integer): "))
    print(f"Row with {n} numbers:")
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    matrix = np.array(matrix, dtype=np.int)
    return matrix


if __name__ == "__main__":
    choice = input("Encrypt, Decrypt or Find Key [e/d/f]: ")
    text = input("Text: ").upper()
    if choice == "e":
        key = makeKey()
        print(hill_cipher(text, key, "encrypt"))
    elif choice == "d":
        key = makeKey()
        print(hill_cipher(text, key, "decrypt"))
    else:
        encoded_message = input("Encrypted message: ")
        m = int(input("m: "))
        print(findK(text, encoded_message, m))