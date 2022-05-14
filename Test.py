import math

Binary = "1,0"
Hexadecimal = "1,2,3,4,5,6,7,8,9,A,B.C.D.E.F"
Decimal = "1,2,3,4,5,6,,7,8,9,10"
Octal = "1,,2,3,4,5,6,7,10"

# Hexadecimal BASE of (16)


Addition = "+"
# This line adds to the equation
Subtraction = "-"
# This line subtracts from the equation
Divide = "/"
# This line divides two numbers also I had to Google how to write the divide sign and its (alt + 0247)
Multiply = "*"

Square_root = "sqrt"
# ALT + 251

while True:
    First_num = input("Please enter you're first number :")
    if First_num == "Q" or First_num == "q":
        print("Application ended thank you")
        break


    Symbol = input(Binary + Hexadecimal + Divide + Decimal + Octal + Addition + Square_root + Subtraction + Multiply + ":")

    Second_num = input("Please enter you're second number :")

    if Symbol == "+":
        print(First_num, "+", Second_num, "=", (int(First_num) + int(Second_num)))
    elif Symbol == "*":
        print(First_num, "*", Second_num, "=", (int(First_num) * int(Second_num)))

    elif Symbol == "-":
        print(First_num, "-", Second_num, "=", (int(First_num) - int(Second_num)))
    elif Symbol == "/":
        print(First_num, "/", Second_num, "=", (float(First_num) / float(Second_num)))
    print("Press Q or q to exit")




