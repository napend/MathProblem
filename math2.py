#This app does your math


addition = input("Print your math sign, +, -, *, /: ")

if addition == "+":
    a = int(input("First Number: "))
    b = int(input("Seccond Number: "))
    c = a + b
    print(c)

elif addition == "-":
    a = int(input("First Number: "))
    b = int(input("Seccond Number: "))
    c = a - b
    print(c)

elif addition == "*":
    a = int(input("First Number: "))
    b = int(input("Seccond Number: "))
    c = a * b
    print(c)

elif addition == "/":
    a = int(input("First Number: "))
    b = int(input("Seccond Number: "))
    c = a / b
    print(c)


else:
    print("That is not a valid operation. Please do +, -, *, /")
