def show_grade_criteria():
    print("--- Grade Criteria ---")
    print("90 - 100 : Grade S")
    print("80 - 89  : Grade A")
    print("65 - 79  : Grade B")
    print("50 - 64  : Grade C")
    print("40 - 49  : Grade D")
    print("Below 40 : Grade F")
    print("----------------------\n")

def show_student_details():
    print("--- Student Details ---")
    print("Name: Rashi Nayak")
    print("Department: BCA")
    print("Semester: 3\n")

def show_subject_marks():
    print("--- Subject Marks ---")
    print("Subject 1: 85")
    print("Subject 2: 90")
    print("Subject 3: 95\n")

def calculate_average():
    return (85 + 90 + 95) / 3

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
    show_subject_marks()
    avg = calculate_average()
    print(f"Average Marks: {avg}")
    print(f"Final Grade: {calculate_grade(avg)}")

if __name__ == "__main__":
    main()

