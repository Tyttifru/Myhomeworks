from functions import add_price
import pytest

def test_add_price():

    fix_sell = 150
    sell_for_1km = 70
    adress_to_client = 2

    expected = 290

    actual = add_price(adress_to_client, fix_sell, sell_for_1km)

    assert expected == actual

@pytest.mark.parametrize("adress_to_client, fix_sell, sell_for_1km, expected", 
    [
    (3,150,70,360),
    (4,150,70,430),
    (5,150,70,500)
    ])
def test_add_price_parametrized(adress_to_client, fix_sell, sell_for_1km, expected):

    actual = add_price(adress_to_client, fix_sell, sell_for_1km)

    assert expected == actual

from functions import prime_sell 
import pytest

@pytest.mark.parametrize("plan_sell, sell, expected", 
    [
    (1000, 2000, 100),       # 10% от 1000 = 100
    (1000, 1000, 0),         # 0
    (1000, 800, -20),        # 10% от -200 = -2
    (200000, 500000, 30000), # 10% от 300000 = 30000
    ])

def test_prime_sell_parametrize(plan_sell, sell, expected):

    actual = prime_sell(plan_sell, sell)

    assert actual == expected

from functions import prib_ot_vklada
import pytest

@pytest.mark.parametrize("summ_vklad, term_vklad, expected", 
    [
    (10000, 18, 1500.0),      # 10% годовых за 18 месяцев (большой вклад)
    (100, 18, 15.0),          # 100 за 18 месяцев (маленький вклад)
    (10000, 0, 0.0),          # 0 месяцев (анализ граничных значений)
    (0, 18, 0.0),             # 0 сумма (анализ граничных значений)
    ])

def test_prib_ot_vklada_parametrize(summ_vklad, term_vklad, expected):
    actual = prib_ot_vklada(summ_vklad, term_vklad)
    assert actual == expected
