from list_comprehensions import coordinates_not_summing_to


def test_sample_0():
    assert coordinates_not_summing_to(1, 1, 1, 2) == [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 1],
    ]


def test_sample_1():
    result = coordinates_not_summing_to(2, 2, 2, 2)
    assert result == [
        [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2],
        [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2],
        [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2],
    ]
