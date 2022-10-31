import one



def test_add():
    assert one.add(3, 4) == 7


def test_subtract():
    assert one.subtarct(4, 5) == -1


def test_multiply():
    assert one.multiply(3, 4) != 11


def test_division():
    assert one.division(50, 5) == 10