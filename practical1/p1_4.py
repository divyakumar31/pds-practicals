"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.4: Write a program in python to implement menu driven simple calculator.
"""

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentioal\n6. Exit")
while True:
    ch = int(input("Enter your choice: "))
    if ch not in range(1, 7):
        print("Enter valid input.")
    elif ch == 5:
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter power: "))
        print(num1**num2)
    elif ch == 6:
        break
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if ch == 1:
            print(num1 + num2)
        elif ch == 2:
            print(num1 - num2)
        elif ch == 3:
            print(num1 * num2)
        elif ch == 4:
            print(num1 / num2)

print("Bye...")