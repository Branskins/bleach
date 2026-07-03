from runner_up_score import runner_up_score


def test_sample():
    assert runner_up_score([2, 3, 6, 6, 5]) == 5


def test_all_same_but_one():
    assert runner_up_score([1, 1, 1, 2]) == 1


def test_two_elements():
    assert runner_up_score([10, 20]) == 10
