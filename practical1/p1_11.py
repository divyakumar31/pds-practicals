"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.11: Write a python program to find occurrence of an element in the list.
"""

items = []

for _ in range(10):
    items.append(input(f"Enter the item {_ + 1}: "))

num = input("Enter the number to find occurence: ")
print(items.count(num))