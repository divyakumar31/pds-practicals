"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.10: Write a program to count a total number of lines and count the total number of lines starting with 'PDS' from the given text file.
"""

filename = input("Enter the filename you want to read: ")

with open(filename, 'r') as fname:
    lines = fname.readlines()
    print(f"Total number of lines in file: {len(lines)}")

    count = 0
    for line in lines:
        if line.startswith('PDS'):
            count += 1

    print(f"Total number of lines starts with \'PDS\': {count}")

fname.close()