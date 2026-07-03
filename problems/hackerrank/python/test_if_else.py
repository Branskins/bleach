import pytest

from if_else import weird_or_not


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, "Weird"),
        (24, "Not Weird"),
        (1, "Weird"),
        (2, "Not Weird"),
        (4, "Not Weird"),
        (6, "Weird"),
        (20, "Weird"),
        (22, "Not Weird"),
        (100, "Not Weird"),
    ],
)
def test_weird_or_not(n, expected):
    assert weird_or_not(n) == expected
