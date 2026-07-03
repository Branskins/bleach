def average_marks(scores: list[float]) -> float:
    return sum(scores) / len(scores)


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(f"{average_marks(student_marks[query_name]):.2f}")
