h = lambda x: f"{(x**2 % 2**8):08b}"[2:6]

hmac = lambda message, K, ipad, opad: h(
    int(
        f"{(int(K, 2) ^ int(opad, 2)):04b}"
        + h(int(f"{(int(K, 2) ^ int(ipad, 2)):04b}" + message, 2)),
        2,
    )
)


if __name__ == "__main__":
    K = input("K: ")
    ipad = input("ipad: ")
    opad = input("opad: ")
    message = input("message: ")

    print(hmac(message, K, ipad, opad))