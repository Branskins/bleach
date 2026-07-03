def print_1_to_n(n: int) -> None:
    for i in range(1, n + 1):
        print(i, end="")


if __name__ == "__main__":
    n = int(input())
    print_1_to_n(n)
