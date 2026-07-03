def integer_and_float_division(a: int, b: int) -> tuple[int, float]:
    return a // b, a / b


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    int_div, float_div = integer_and_float_division(a, b)
    print(int_div)
    print(float_div)
