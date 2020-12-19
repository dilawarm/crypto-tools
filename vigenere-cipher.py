import string
import operator

ALPHABET = string.ascii_uppercase + "ÆØÅ"


def vigenere(plaintext, key, algo):
    op = operator.add if algo.lower() == "encrypt" else operator.sub
    return "".join(
        ALPHABET[
            (
                op(
                    ALPHABET.index(plaintext[i].upper()),
                    ALPHABET.index(key[i % len(key)].upper()),
                )
            )
            % len(ALPHABET)
        ]
        for i in range(len(plaintext))
        if plaintext[i] != " "
    )


if __name__ == "__main__":
    choice = input("Encrypt or Decrypt [e/d]: ")
    text = input("Text: ").upper()
    key = input("Key: ").upper()
    if choice == "e":
        print(vigenere(text, key, "encrypt"))
    else:
        print(vigenere(text, key, "decrypt"))