import pytest
from Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 500)
    checkout.add_item_price("b", 1)
    return checkout


# def test_calculate_total(checkout):
#     checkout.add_item_price("a", 500)
#     checkout.add_item("a")
#     assert checkout.calculate_total() == 500


def test_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 501


def test_add_discount(checkout):
    checkout.add_discount("a", 3, 2)


# @pytest.mark.skip
def test_apply_discount(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2


def test_item_exception(checkout):
    with pytest.raises(Exception):
        checkout.add_item("c")
