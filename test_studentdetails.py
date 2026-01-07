import pytest
import studentdetails


@pytest.mark.parametrize(
    "marks, expected_grade",
    [
        ([90, 95, 100], "S"),   # S grade
        ([90, 90, 90], "S"),    # S lower boundary
        ([85, 88, 82], "A"),    # A middle
        ([80, 80, 80], "A"),    # A boundary
        ([70, 75, 78], "B"),    # B middle
        ([65, 65, 65], "B"),    # B boundary
        ([55, 58, 60], "C"),    # C middle
        ([50, 50, 50], "C"),    # C boundary
        ([45, 48, 42], "D"),    # D middle
        ([40, 40, 40], "D"),    # D boundary
        ([30, 35, 20], "F"),    # F below 40
        ([0, 0, 0], "F"),       # Zero marks
        ([89, 88, 87], "A"),    # Upper A
        ([79, 78, 77], "B"),    # Upper B
        ([64, 63, 62], "C"),    # Upper C
        ([49, 48, 47], "D"),    # Upper D
    ]
)
def test_calculate_grade_parameterized(marks, expected_grade):
    avg = studentdetails.calculate_average(marks)
    grade = studentdetails.calculate_grade(avg)
    assert grade == expected_grade
