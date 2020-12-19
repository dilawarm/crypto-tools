import string

ALPHABET = string.ascii_uppercase + "ÆØÅ"


def autokey(text, key, algo):
    op = 1 if algo == "encrypt" else -1
    out = ""
    k = key
    for t in text:
        if op == 1:
            index = ALPHABET.index(t)
        else:
            index = t

        res = op * k + index
        out += ALPHABET[(op * k + index) % len(ALPHABET)]

        if op == 1:
            k = index
        else:
            k = res

    return out


if __name__ == "__main__":
    choice = input("Encrypt or Decrypt [e/d]: ")
    key = int(input("Key: "))
    if choice == "e":
        text = input("Text: ").upper()
        print(autokey(text, key, "encrypt"))
    else:
        text = [int(x) for x in input("Numbers: ").split()]
        print(autokey(text, key, "decrypt"))