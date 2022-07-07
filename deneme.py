
def calculate(num1, num2, num3):

    symbol = input("enter symbool :")
    if symbol == "+":
        print(num1 + num2 +num3)
    elif symbol == "-":
        print(num1 - num2 -num3)
    elif symbol == "/":
        print(num1 / num2 / num3)
    else:
        print(num1 * num2 *num3)
print(calculate(4, 5, 6))