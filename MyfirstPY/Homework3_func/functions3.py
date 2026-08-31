def employee_rating(reit_list: list) -> int:
    '''
    Для премирования компания использует систему рейтинга сотрудников. Наибольшую премию
    получает сотрудник с самым высоким рейтингом.
    Функция получает на вход список чисел (рейтинг сотрудников) и возвращает
    наибольшее из значений.

    Аргументы: reit_list(list) - рандомный список чисел (рейтингов)

    Возвращает: Наиболее число (рейтинг) в списке
    '''

    max_reit = reit_list [0]
    for i in reit_list:
        if i > max_reit:
            max_reit = i
    return max_reit

def prices_markup(price_zak: list) -> list: 
    '''
    Интернет магазин занимается перепродажей товаров от поставщиков, при этом добавляя к их
    стоимости наценку в 18%.
    Эта функция получает на вход список закупочных цен и возвращает список с
    ценами после наценки.

    Аргументы: price_zak(list) - рандомный список список цен

    Возвращает: price_end(list) - список цен с наценкой 18%
    '''

    price_end=[]
    percent = 0.18

    for i in price_zak:
        price_end.append(round(i * percent + i, 2))
    return price_end

def failed_plan(plan_sales: int, mans_sales: list) -> int:
    '''
    Функция, которая получает на вход список суммы продаж каждого сотрудника и отдельное
    число - план по продажам. Программа должна возвращать одно значение - число сотрудников не
    выполнивших план.

    Аргументы: \\
    plan_sales(int) - план продаж сотрудника \\
    mans_sales(list) - список сумм продаж сотрудников

    Возвращает: mans(int) - число сотрудников не выполнивших план

    '''

    mans = 0

    for i in mans_sales:
        if i < plan_sales:
            mans +=1
    return mans

def off_doubles(numbers: list) -> list:
    '''
    При регистрации на мероприятие некоторые из участников зарегистрировались несколько раз.
    Организаторам необходимо понимать точное число и список участников.
    Функция, которая получает на вход список с именами участников и
    возвращающую массив участников без дублей.

    Аргументы: numbers(list) - список участников

    Вовзращает: numbers_end(list) - список участников без дублей
    '''
'''
    numbers_end = [] 
    mans = 0

    for i in numbers:
        if i not in numbers_end:
            numbers_end.append(i)
            mans += 1
    return numbers_end, mans
'''
def off_doubles(numbers):
    
    seen = set()
    result = []
    how = 0

    for name in numbers:
        if name not in seen:
            seen.add(name)
            result.append(name)
            how += 1

    return result, how