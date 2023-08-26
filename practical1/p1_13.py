"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.13: Create a tuple to store value of student's marks of pds subject and display it.
"""

def main():
    students = tuple()
    print("1. Add student marks\n2. Display student marks\nPress any key to exit.\n")
    while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            students += store_student()
        elif ch == 2:
            display_student(students)
        else:
            exit("Bye...")



def display_student(students: tuple) -> None:
    if len(students) == 0:
        print("No student exits.")
        return 
    
    print("+==============================+")
    print("| Name                 | Marks |")
    print("+==============================+")

    for student in students:
        print(f"| {student[0]:20} | {student[1]:05.2f} |")
        print("+------------------------------+")
    


def store_student() -> tuple:
    name = input("Enter student name: ")
    marks = float(input("Enter marks of student: "))
    new_student = [[name, marks]]
    return tuple(new_student)


if __name__ == "__main__":
    main()