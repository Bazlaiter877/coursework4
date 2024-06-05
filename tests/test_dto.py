import pytest

from src.dto import Salary


class TestSalaryCompare:

    def test_salary_are_equals_none_with_same_currency(self):
        salary_1 = Salary(salary_from=None, salary_to=None, currency='RUB')
        salary_2 = Salary(salary_from=None, salary_to=None, currency='RUB')

        assert salary_1 == salary_2

    def test_salary_are_equals_not_none_with_same_currency(self):
        salary_1 = Salary(salary_from=100, salary_to=100, currency='RUB')
        salary_2 = Salary(salary_from=100, salary_to=100, currency='RUB')

        assert salary_1 == salary_2

    def test_1(self):
        lower_salary = Salary(salary_from=100, salary_to=None, currency='RUB')
        higher_salary = Salary(salary_from=200, salary_to=None, currency='RUB')

        assert lower_salary < higher_salary

    @pytest.mark.parametrize('not_none_salary', [
        {'salary_from': 100, 'salary_to': None},
        {'salary_from': None, 'salary_to': 200},
        {'salary_from': 100, 'salary_to': 200}
    ])
    def test_2(self, not_none_salary):
        lower_salary = Salary(salary_from=None, salary_to=None, currency='RUB')
        higher_salary = Salary(currency='RUB', **not_none_salary)
