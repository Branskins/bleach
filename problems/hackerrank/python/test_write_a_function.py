import pytest

from write_a_function import is_leap


@pytest.mark.parametrize(
    "year, expected",
    [
        (1990, False),
        (2000, True),
        (2400, True),
        (1800, False),
        (1900, False),
        (2100, False),
        (2004, True),
    ],
)
def test_is_leap(year, expected):
    assert is_leap(year) is expected
