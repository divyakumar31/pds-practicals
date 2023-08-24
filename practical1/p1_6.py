"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.6: Write a Python function to check whether a number is "Perfect" or not. Perform it with and without user defined function. 
"""

def main():
    num = int(input("Enter the number: "))
    isPerfect(num)


def isPerfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print(f"{n} is perfect number.")
    else:
        print(f"{n} is not perfect number.")


if __name__ == "__main__":
    main()