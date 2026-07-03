def sum_difference_product(a: int, b: int) -> tuple[int, int, int]:
    return a + b, a - b, a * b


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    total, difference, product = sum_difference_product(a, b)
    print(total)
    print(difference)
    print(product)
