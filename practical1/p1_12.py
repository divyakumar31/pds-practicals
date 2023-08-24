"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.12: Write a python program to Sort the list according to the column using lambda. Display smallest and largest number from the list. Perform addition of all the members of list and display it. 
"""

def main():
    items = []

    for _ in range(10):
        items.append(int(input(f"Enter the item {_ + 1}: ")))

    items = sort_list(items)
    print(items)
    print("Smallest number from list:", min(items))
    print("Largest number from list:", max(items))
    print("Addition of all members of list:", add_elements(items))


def sort_list(items: list) -> list:
    items = sorted(items, key=lambda x: x)
    return items


def add_elements(items: list) -> int:
    sum = 0
    for item in items:
        sum += item

    return sum


if __name__ == "__main__":
    main()