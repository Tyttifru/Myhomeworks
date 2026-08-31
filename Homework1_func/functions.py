def add_price(adress_to_client: int, fix_sell = 150, sell_for_1km = 70) -> int: 
    '''
    Считает цену доставки

    Аргумент: adress_to_client(int) - Расстояние до клиента

    Фиксированная цена - 150

    Цена на 1 км - 70
    '''

    return adress_to_client * sell_for_1km + fix_sell

def prime_sell(plan_sell: int, sell: int) -> int:
    '''
    Считает размер премии сотрудника, 10% от размера перевыполнения

    Аргументы: plan_sell(int) - план продаж, sell_plan(int) - продажи сотрудника

    Возвращает: размер премии
    '''

    return (sell - plan_sell) * 0.1

def prib_ot_vklada(summ_vklad: int, term_vklad = 18) -> int:
    '''
    Эта функция считает размер прибыли за 18 месяцев от вклада под 10% годовых

    Аргументы: summ_vklad(int) - сумма вклада, срок (term_vklad) - 18 месяцев

    Возвращает: Размер прибыли за 18 месяцев
    '''

    prib_12 = summ_vklad * 0.1 # прибыль за 12 месяцев
    prib_1 = prib_12 / 12 # прибыль за один месяц
    prib = prib_1 * term_vklad

    return prib