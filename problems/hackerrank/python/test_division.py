from division import integer_and_float_division


def test_sample():
    assert integer_and_float_division(4, 3) == (1, 4 / 3)


def test_exact_division():
    assert integer_and_float_division(6, 3) == (2, 2.0)
