from print_function import print_1_to_n


def test_sample(capsys):
    print_1_to_n(3)
    assert capsys.readouterr().out == "123"


def test_n_equals_one(capsys):
    print_1_to_n(1)
    assert capsys.readouterr().out == "1"
