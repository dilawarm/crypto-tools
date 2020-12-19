import string

ALPHABET = string.ascii_uppercase + "ÆØÅ"


def encrypt(message, k):
    enc_message = ""
    for i in range(len(message)):
        for j in range(len(ALPHABET)):
            if message[i] == ALPHABET[j]:
                enc_message += ALPHABET[(j + k) % len(ALPHABET)]
                break
    print(enc_message)


def decrypt(enc_message):
    for k in range(len(ALPHABET)):
        dec_message = ""
        for i in range(len(enc_message)):
            for j in range(len(ALPHABET)):
                if enc_message[i] == ALPHABET[j]:
                    dec_message += ALPHABET[(j - k) % len(ALPHABET)]
                    break
        print(f"Krypteringsnøkkel: {k}, Klartekst: {dec_message}")


if __name__ == "__main__":
    choice = input("Encrypt or Decrypt [e/d]: ")
    text = input("Text: ").upper()
    if choice == "e":
        k = int(input("K: "))
        encrypt(text, k)
    else:
        decrypt(text)