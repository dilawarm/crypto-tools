from square_and_multiply import square_and_multiply

verify = lambda x, y, e, n: square_and_multiply(y, e, n, log=False) == x

create_signed_message = lambda y, e, n: (square_and_multiply(y, e, n, log=False), y)


def known_message_attack(messages, n):
    x, y = 1, 1
    for message in messages:
        x *= message[0]
        y *= message[1]
    return (x % n, y % n)


encrypt_and_sign = lambda x, e, d, n, n_alice: (
    square_and_multiply(x, e, n, log=False),
    square_and_multiply(square_and_multiply(x, d, n_alice, log=False), e, n, log=False),
)

if __name__ == "__main__":
    choice = input(
        """
        Verify [v]
        Fake signed message [f]
        Known message attack [k]
        Encrypt and sign message: [e]
        """
    )
    p = int(input("p: "))
    q = int(input("q: "))
    e = int(input("e: "))
    n = p * q
    if choice == "v":
        x = int(input("x: "))
        y = int(input("y: "))
        print(verify(x, y, e, n))
    elif choice == "f":
        y = int(input("y: "))
        signature = create_signed_message(y, e, n)
        print(signature)
        print(verify(signature[0], signature[1], e, n))
    elif choice == "k":
        total_messages = int(input("Total messages: "))
        messages = []
        for _ in range(total_messages):
            x, y = [int(i) for i in input("x,y: ").split(",")]
            messages.append((x, y))
        message = known_message_attack(messages, n)
        print(message)
        print(verify(message[0], message[1], e, n))
    else:
        p_alice = int(input("p: "))
        q_alice = int(input("q: "))
        n_alice = p_alice * q_alice

        d = int(input("d: "))
        x = int(input("x: "))

        print(encrypt_and_sign(x, e, d, n, n_alice))
