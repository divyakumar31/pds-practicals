"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.9: Write a program to find Highest Common Factor (HCF) and Greatest Common Divisor (GCD) of two numbers using function.
"""

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"GCD of {num1} and {num2} is", calculate_gcd(num1, num2))


def calculate_gcd(num1: int, num2: int) -> int:
    """
    This function is used to find Greatest Common Divisior of two numbers.
    """
    smaller = min(num1, num2)
    for i in range(1, smaller+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            gcd = i 
    return gcd


if __name__ == "__main__":
    main()