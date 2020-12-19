cipher = lambda x: f"{((x+3) % 2**4):04b}"  # BYTT UT CIPHER HER :)


def cbc_mac(message):
    message = message.split()
    y = "0000"
    for mes in message:
        y = cipher(int(f"{(int(y, 2) ^ int(mes, 2)):04b}", 2))
    return y


if __name__ == "__main__":
    message = input("Message: ")
    print(cbc_mac(message))