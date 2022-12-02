num = 71


def main():
    global num
    while num != 1:  # Use while num != 1
        # Rules:
        if num % 2 == 0:  # Check parity
            num = num / 2
            print(int(num))

        elif num % 2 != 0:
            num = num * 3 + 1
            print(int(num))


main()
