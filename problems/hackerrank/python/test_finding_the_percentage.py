from finding_the_percentage import average_marks


def test_sample_0():
    assert round(average_marks([52, 56, 60]), 2) == 56.00


def test_sample_1():
    assert round(average_marks([25, 26.5, 28]), 2) == 26.50
