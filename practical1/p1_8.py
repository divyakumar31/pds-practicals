"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.8: Write a Python function to check whether a string is a pangram or not.
"""

def main():
    sentence = input("Enter the string: ")
    if isPangram(sentence):
        print(f"\"{sentence}\" is pangram.")
    else:
        print(f"\"{sentence}\" is not pangram.")


def isPangram(s):
    s = s.lower()
    ch = ord('a')
    while ch <= ord('z'):
        if chr(ch) not in s:
            return False
        ch += 1
    return True


if __name__ == "__main__":
    main()