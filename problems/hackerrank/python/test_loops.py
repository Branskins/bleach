from loops import squares_below


def test_sample():
    assert squares_below(5) == [0, 1, 4, 9, 16]


def test_zero():
    assert squares_below(0) == []
