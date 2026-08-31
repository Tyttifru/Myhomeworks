from task4_tuple import calculate_total
import pytest

def test_calculate_total():

    receipt =  [
    ("Сыр", 2, 250),
    ("Макароны", 3, 80),
    ("Кофе", 1, 300),
    ("Чай", 1, 150)
    ]
    expected = 1190

    actual = calculate_total(receipt)

    assert actual == expected
    
@pytest.mark.parametrize("receipt, expected", 
    [
    ([], 0),
    ([("Хлеб", 2, 50)], 100),
    ([("Сыр", 0, 250), ("Хлеб", 2, 50)], 100),
    ([("Смартфон", 1, 50000), ("Автомобиль", 1, 750000)], 800000),
    ])

def test_calculate_total_parametrize(receipt, expected):

    actual = calculate_total(receipt)

    assert actual == expected
