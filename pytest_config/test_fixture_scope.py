import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_module2():
    print("\nSetup module2")


@pytest.fixture(scope="class", autouse=True)
def setup_class2():
    print("\nSetup class2")


@pytest.fixture(scope="function", autouse=True)
def setup_function2():
    print("\nSetup function2")


class TestClass:
    def test_it(self):
        print("TestIt")
        assert True

    def test_it2(self):
        print("TestIt2")
        assert True
