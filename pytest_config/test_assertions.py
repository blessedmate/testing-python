from pytest import approx, raises


def test_float():
    # Python doesn't do exact maths like this
    # assert (0.1 + 0.2) == 0.3
    assert (0.1 + 0.2) == approx(0.3)


def raises_value_exception():
    raise ValueError


def test_exception():
    with raises(ValueError):
        raises_value_exception()
