"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.2:  Ram wants to know age of his grandfather, who was born on 18th December, 1950. Kindly help ram to know how old is his grandfather? Also, print the calendar for the month and year on which ram's grandfather was born. 
"""

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
import calendar



year = int(input("Enter the birth year: "))
month = int(input("Enter the birth month: "))
day = int(input("Enter the birth day: "))
birth_date = datetime(year, month, day).date()
print(calendar.month(year, month))

current_date = datetime.now().date()
age = relativedelta(current_date, birth_date)

print(f"Current age of Ram's grandfather is {age.years} years, {age.months} months and {age.days} days.")