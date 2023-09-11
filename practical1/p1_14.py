"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.14: Write a program to create a set of students' enrolment number and sort them and display it.
"""

def main():
    students = set()
    print("1. Add students' enrolment number\n2. Display students in sorted order\nPress any key to exit.\n")
    while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            students = add_student(students)
        elif ch == 2:
            display_set(students)
        else:
            exit("Bye...")


def add_student(students: set) -> set:
    enroll = int(input("Enter student enroll no.: "))
    students.add(enroll)
    return students


def display_set(students: set) -> None:
    if len(students) == 0:
        print("No student exists.")
        return 

    sorted_students = sort_set(students)
    for student in sorted_students:
        print(student)


def sort_set(students: set) -> list:
    return sorted(students, key=lambda x:x)


if __name__ == "__main__":
    main()