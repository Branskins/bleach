def second_lowest_grade_names(students: list[list]) -> list[str]:
    grades = sorted({grade for _, grade in students})
    second_lowest = grades[1]
    names = [name for name, grade in students if grade == second_lowest]
    return sorted(names)


if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    for name in second_lowest_grade_names(students):
        print(name)
