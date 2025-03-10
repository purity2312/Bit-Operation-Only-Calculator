import time

mask = 0xFFFFFFFF   # 32 bit mask
def add(num1, num2):
    while (num2 & mask):
        c = (num1 & num2) # carry
        s = (num1 ^ num2) # sum
        num1 = s
        num2 = c << 1

    if num2 > 0:
        return num1 & mask
    return num1


def subtract(num1, num2):
    # Negate num2 using two's complement
    num2 = add(~num2, 1)

    return add(num1, num2)


def multiply(num1, num2):
    res = 0
    negative = False
    #negate num2 using two's complement if it is < 0
    if num2 < 0:
        negative = True
        num2 = add(~num2, 1)

    while num2:
        # If num2 is odd, add num1 to the result
        if num2 & 1:
            res = add(res, num1)
        num1 = num1 << 1 # Double num1
        num2 = num2 >> 1 # Halve num2

    if negative:
        res = add(~res, 1)
    return res

def divide(num1, num2):
    if num2 == 0:
        return "undefined"
    if num1 == 0:
        return 0

    quotient = 0
    negative = (num1 < 0) ^ (num2 < 0)

    if num1 < 0:
        num1 = add(~num1, 1)
    if num2 < 0:
        num2 = add(~num2, 1)

    while num1 >= num2:
        temp = num2
        multiple = 1

        # double temp until it exceeds num1
        while (temp << 1) <= num1:
            temp = temp << 1
            multiple = multiple << 1

        # subtract the largest chunk found in num1
        num1 = subtract(num1, temp)
        quotient = add(quotient, multiple)

    if negative:
        quotient = add(~quotient, 1)
    return quotient

def display_menu():
    print("Please select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    display_menu()
    select = int(input("Select an operation: "))
    if select == 5:
        print("\nThank you for using the program.")
        break

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
        res = add(number_1, number_2)
        print(number_1, "+", number_2, "=", res)
    elif select == 2:
        res = subtract(number_1, number_2)
        print(number_1, "-", number_2, "=", res)
    elif select == 3:
        res = multiply(number_1, number_2)
        print(number_1, "*", number_2, "=", res)
    elif select == 4:
        res = divide(number_1, number_2)
        print(number_1, "/", number_2, "=", res)
    else:
        print("Invalid selection.")
    print()
    time.sleep(1)

