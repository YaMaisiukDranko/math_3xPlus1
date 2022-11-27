initialNum = int(input("Initial Number:  "))
num = initialNum
while num != 1:
    if num % 2 == 0:
        num /= 2
        print(int(num))
    else:
        num = num * 3 + 1
        print(int(num))

print("Next number")