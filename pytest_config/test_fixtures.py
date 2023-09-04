import pytest


@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")


# def test_1(setup):
def test_1():
    print("Executing test1")
    assert True


# @pytest.mark.usefixtures("setup")
def test_2():
    print("Executing test2")
    assert True
