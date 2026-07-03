from nested_lists import second_lowest_grade_names


def test_sample():
    students = [
        ["Harry", 37.21],
        ["Berry", 37.21],
        ["Tina", 37.2],
        ["Akriti", 41],
        ["Harsh", 39],
    ]
    assert second_lowest_grade_names(students) == ["Berry", "Harry"]


def test_single_second_lowest():
    students = [["A", 1.0], ["B", 2.0], ["C", 3.0]]
    assert second_lowest_grade_names(students) == ["B"]
