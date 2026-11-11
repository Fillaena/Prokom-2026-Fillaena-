# tes dengan fixture
import pytest
from exercise11_3_functions import Employee


@pytest.fixture
def employee():
    """An Employee instance available to all test functions."""
    return Employee('Fillaena', 'Bipta', 60000)


def test_give_default_raise(employee):
    """Does a default raise of $5,000 work?"""
    employee.give_raise()
    assert employee.annual_salary == 65000


def test_give_custom_raise(employee):
    """Does a custom raise work?"""
    employee.give_raise(10000)
    assert employee.annual_salary == 70000