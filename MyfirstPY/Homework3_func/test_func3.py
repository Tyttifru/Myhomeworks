from functions3 import off_doubles
import pytest

@pytest.mark.parametrize("numbers, expected, numbers_quantity", 
    [
    (["Роман", "Роман", "Юлия", "Роман", "Юлия", "Софья"], ["Роман", "Юлия", "Софья"], 3),
    (["Сергей", "Александр", "Василий"], ["Сергей", "Александр", "Василий"], 3),
    (["Анна", "Анна", "Анна"], ["Анна"], 1),
    ([], [], 0),
    ])
def test_off_doubles_parametrize(numbers, expected, numbers_quantity):

    actual_list, actual_quantity = off_doubles(numbers)

    assert actual_list == expected
    assert actual_quantity == numbers_quantity

from functions3 import employee_rating
import pytest

@pytest.mark.parametrize("input_list, expected", 
    [
    ([1, 2, 3, 4, 5], 5),
    ([0, 0, 0, 1, 0], 1),
    ([-100, 0, 100], 100),
    ])

def test_parametrized_employee_rating(input_list, expected):
    
    assert employee_rating(input_list) == expected

from functions3 import failed_plan
import pytest

@pytest.mark.parametrize("plan, sales, expected", 
    [
    (100, [50, 60, 70, 80, 90], 5),  # все не выполнили
    (100, [100, 110, 120, 130, 140], 0),  # все выполнили
    (100, [50, 100, 150, 200], 1)  # один не выполнил
    ])

def test_parametrized_failed_plan(plan, sales, expected):

    assert failed_plan(plan, sales) == expected