from arithmetic_operators import sum_difference_product


def test_sample():
    assert sum_difference_product(3, 2) == (5, 1, 6)


def test_negative_difference():
    assert sum_difference_product(2, 3) == (5, -1, 6)


def test_zero():
    assert sum_difference_product(0, 0) == (0, 0, 0)
