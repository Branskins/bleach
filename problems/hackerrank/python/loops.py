def squares_below(n: int) -> list[int]:
    return [i * i for i in range(n)]


if __name__ == "__main__":
    n = int(input())
    for square in squares_below(n):
        print(square)
