import sys

def show_grade_criteria():
    print("\n--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------")


def show_student_details():
    print("\n--- Student Details ---")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    print("\nStudent Information")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)


def show_subject_marks():
    print("\n--- Enter Subject Marks ---")
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)
    return marks


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


def main():
    show_grade_criteria()
    show_student_details()
    marks = show_subject_marks()

    avg = calculate_average(marks)
    grade = calculate_grade(avg)

    print("\n--- Result ---")
    print(f"Average Marks: {avg:.2f}")
    print(f"Final Grade: {grade}")



if __name__ == "__main__":
    if sys.stdin.isatty():   # real user typing
        main()
    else:
        print("CI/CD environment detected. User input skipped.")
