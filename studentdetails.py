import sys
import os

def show_grade_criteria():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------")


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main_interactive():
    # LOCAL USER INPUT
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sem = input("Enter Semester: ")

    marks = []
    for i in range(1, 4):
        marks.append(float(input(f"Enter marks for Subject {i}: ")))

    return name, dept, sem, marks


def main_ci():
    # JENKINS / DOCKER USER INPUT
    name = os.environ.get("NAME")
    dept = os.environ.get("DEPT")
    sem = os.environ.get("SEM")
    marks = list(map(float, os.environ.get("MARKS").split(",")))

    return name, dept, sem, marks


def main():
    show_grade_criteria()

    if sys.stdin.isatty():
        name, dept, sem, marks = main_interactive()
    else:
        name, dept, sem, marks = main_ci()

    avg = calculate_average(marks)
    grade = calculate_grade(avg)

    print("\n--- Student Details ---")
    print("Name:", name)
    print("Department:", dept)
    print("Semester:", sem)

    print("\n--- Result ---")
    print(f"Average Marks: {avg:.2f}")
    print(f"Final Grade: {grade}")


if __name__ == "__main__":
    main()
