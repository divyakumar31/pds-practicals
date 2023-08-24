"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.3:   Write a Python program to create 12 fixed dates from a specified date over a given period. The difference between two dates is 10. 
"""

from datetime import datetime, timedelta


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
specified_date = datetime(year, month, day).date()

for i in range(12):
    specified_date = specified_date + timedelta(days = 10)
    print(f"Date after {(i+1)*10} days is {specified_date}.")