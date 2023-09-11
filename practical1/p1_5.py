"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.5: Write a program which will allow user to enter 10 numbers and display largest odd number from them. It will display appropriate message in case if no odd number is found and display count of odd numbers. 
"""
# from pandas import array as arr
evenCount = 0
oddCount = 0

arr = []
for n in range(10):
    num = int(input(f"Enter {n}th number: "))
    arr.append(num)


largestEven = largestOdd = arr[0]
for n in range(10):
    if arr[n]%2 == 0:
        evenCount = evenCount + 1
        if largestEven < arr[n]:
            largestEven = arr[n]
    else:
        oddCount = oddCount + 1
        if largestOdd < arr[n]:
            largestOdd = arr[n]

print(f"Largest Even number is {largestEven}")
print(f"Largest Odd number is {largestOdd}")
print(f"Total Odd numbers is {oddCount}")
print(f"Total Even numbers is {evenCount}")

# n,k=map(int,input().split())