# tes tanpa fixture
from exercise11_3_functions import Employee


def test_give_default_raise():
    """Does a default raise of $5,000 work?"""
    employee = Employee('Fillaena', 'Bipta', 60000)
    employee.give_raise()
    assert employee.annual_salary == 65000


def test_give_custom_raise():
    """Does a custom raise work?"""
    employee = Employee('Fillaena', 'Bipta', 60000)
    employee.give_raise(10000)
    assert employee.annual_salary == 70000
    
