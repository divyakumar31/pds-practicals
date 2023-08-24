"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.7: Write a Python function to print first n rows of Pascal's triangle.
"""
from math import comb

def main():
    height = int(input("Enter the height of Pascal's triangle: "))
    pascalTriangle(height)


def pascalTriangle(n):
    if n <= 0:
        print("Height should be valid.")
    elif n == 1:
        print(1)
    else:
        print("  " * n, end="")
        print(1)
        for i in range(1, n):
            print("  " * (n - i), end="")
            for j in range(i):
                print(comb(i, j), end="   ")
            print(1)


if __name__ == "__main__":
    main()