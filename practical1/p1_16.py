"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.16: Write a program to create a dictionary of student details and perform basic operation on it.
"""

def main():
    students = {}
    print("1. Add student \n2. Display student details \n3. Remove student details \nPress any key to exit.\n")
    while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            students = add_student(students)
        elif ch == 2:
            display_student(students)
        elif ch == 3:
            remove_student(students)
        else:
            exit("Bye...")


def add_student(students: dict) -> dict:
    enroll = int(input("Enter student enrollment number: "))
    name = input("Enter student name: ")
    students[enroll] = name
    return students



def display_student(students: dict) -> None:
    if len(students) == 0:
        print("No student exists.")
        return 
    
    print("+=====================================+")
    print("| Name                 | enrollment   |")
    print("+=====================================+")

    for student in students.items():
        print(f"| {student[1]:20} | {student[0]:12} |")
        print("+-------------------------------------+")
    



def remove_student(students: dict) -> dict:
    if len(students) == 0:
        print("No student exists.")
        return 
    
    enroll = int(input("Enter student\'s enrollment number to remove: "))
    del students[enroll]
    


if __name__ == "__main__":
    main()