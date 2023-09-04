# Automatically called once before setting up functions when using pytest
# similar to setup_class
def setup_module(module):
    print("Setup module!")


# Automatically called once after tearing down functions when using pytest
# similar to teardown_class
def teardown_module(module):
    print("Teardown module!")


# Automatically called before every test function when using pytest
def setup_function(function):
    if function == test1:
        print("\nSetting up test 1")
    elif function == test2:
        print("\nSetting up test 2")
    else:
        print("\nUnknown setup")


# Automatically called after every test function when using pytest
def teardown_function(function):
    if function == test1:
        print("\nTearing down test 1")
    elif function == test2:
        print("\nTearing down test 2")
    else:
        print("\nUnknown teardown")


def test1():
    print("Executing test1")
    assert True


def test2():
    print("Executing test2")
    assert True
