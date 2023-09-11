"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.18: Write a program to list of objects of dictionary of student details sort them according to the SPI of students.   
"""

def main():
    students = {}
    print("1. Add student \n2. Display student details(sorted) \nPress any key to exit.\n")
    while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            students = add_student(students)
        elif ch == 2:
            display_student(students)
        else:
            exit("Bye...")


def add_student(students: dict) -> dict:
    enroll = int(input("Enter student enrollment number: "))
    name = input("Enter student name: ")
    spi = float(input("Enter student SPI: "))
    students[enroll] = [name, spi]
    return students



def display_student(students: dict) -> None:
    if len(students) == 0:
        print("No student exits.")
        return 
    
    print("+=============================================+")
    print("| Name                 | enrollment   | SPI   |")
    print("+=============================================+")

    students = sort_student(students)
    
    for student in students.items():
        print(f"| {student[1][0]:20} | {student[0]:12} | {student[1][1]:05.2f} |")
        print("+---------------------------------------------+")
    

def sort_student(students: dict) -> dict:
    students = dict(sorted(students.items(), key=lambda x:x[1][1]))
    return students



if __name__ == "__main__":
    main()