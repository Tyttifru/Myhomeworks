from functions2 import suitable_table
import pytest

@pytest.mark.parametrize("table, expected", 
    [
    (1, "Маленький стол"),
    (2, "Маленький стол"),
    (3, "Средний стол"),
    (6, "Большой стол"),
    (10, "Гуляй, Вуася")
    ])
def test_suitable_table_parametrized(table, expected):

    actual = suitable_table(table)

    assert actual == expected
    
from functions2 import discount_or_not
import pytest

@pytest.mark.parametrize("age_client, quantity_orders, summ_orders, expected", 
    [
    (60, 0, 0, True),           # 60 лет
    (61, 0, 0, True),           # 61 год
    (59, 4, 5000, True),        # 4 заказа ровно на 5000
    (59, 10, 10000, True),      # много заказов, большая сумма
    (30, 3, 10000, False),      # 3 заказа, большая сумма
    (40, 10, 4000, False),      # много заказов, но сумма маленькая
    (30, 2, 1000, False),       # мало заказов, малая сумма
    ])
def test_discount_or_not_various_cases(age_client, quantity_orders, summ_orders, expected):
        
        result = discount_or_not(age_client, quantity_orders, summ_orders)

        assert result == expected

from functions2 import in_size
import pytest

@pytest.mark.parametrize("length, width, height, mass, distance, expected", 
    [
    (10, 10, 10, 5, 5, True), # Идеальные параметры (True)
    (50, 50, 50, 10, 3, True), # Граничные значения (True)
    (100, 100, 100, 5, 5, False),   # Превышение суммы измерений
    (200, 10, 10, 5, 5, False),     # Превышение одного из измерений
    (50, 50, 50, 15, 5, False),     # Превышение массы
    (50, 50, 50, 5, 2, False),      # Маленькое расстояние (2 < 3)
    (50, 50, 50, 5, 11, False),     # Большое расстояние(11 > 10)
    ])
def test_in_size_various_cases(length, width, height, mass, distance, expected):

        result = in_size(length, width, height, mass, distance)

        assert result == expected
