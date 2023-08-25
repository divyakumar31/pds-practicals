"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.15: Write a program to perform add, delete, union, intersection, difference, and symmetric difference and membership testing operation for the given sets.  
"""

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20}

set2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

set3 = {5, 10, 15, 20}

set4 = {50, 100, 150}

print("Set 1:", set1, "\nSet 2:", set2, "\nSet 3:", set3, "\nSet 4:", set4, end="\n\n")
set3.add(16)
print("Add 16 in set3:", set3)

set3.discard(16)
print("Delete 16 from set3:", set3)

print("Union of set2 and set3:", set3.union(set2))

print("Intersection of set1 and set2:", set1.intersection(set2))

# difference
print("Difference of set3 and set2:", set3.difference(set2))

# symmetric difference 
print("Symmetric difference of set3 and set2:", set3.symmetric_difference(set2))

# membership testing operation
print("Is set3 subset of set2?:", set3.issubset(set2))

print("Is set3 subset of set1?:", set3.issubset(set1))

print("Intersection of set3 and set4:", set3.intersection(set4))

print("Is set3 and set4 disjoint set?:", set3.isdisjoint(set4))