def action_price (price_product: int, quantity_product: int, in_action: bool):
    '''
    Функция, которая считает скидку по следующим правилам:
    Если количество товара в чеке больше либо равно 5, то к товару применяется скидка в
    10%. Если товар учавствует в акции - применяется скидка в 15%. Скидки могут
    суммироваться.
    
    Аргументы: \\
    price_product(int) - Цена товара \\
    quantity_product(int) - Количество товара \\
    in_action(bool) - Участвует в акции? (да/нет)

    Возвращает: Название товара, количество, цену с учетом скидки, размер скидки.

    '''

    total_price = price_product * quantity_product
    action = 0

    if in_action == "да":
        in_action = True
    else:
        in_action = False

    if quantity_product >= 5 and in_action:
        total_price = int(total_price * 0.75)
        action = 25
    elif quantity_product >= 5 and not in_action:
        action = int(total_price * 0.9)
        action = 10
    elif quantity_product < 5 and in_action:
        total_price = int(total_price * 0.85)
        action = 15
    
    return total_price, action

def suitable_table (table: int) -> str:
    '''
    Функция, которая получает количество гостей и
    предлагает наиболее подходящий стол.

    Аргументы: table(int) - количество гостей

    Возвращает: Подходящий стол или отсутвие возможности разместить.
    '''

    result = 0

    if table <= 2:
        result = ("Маленький стол")
    elif table <=4:
        result = ("Средний стол")
    elif table <=8:
        result = ("Большой стол")
    else:
         result = ("Гуляй, Вуася")
    return result

def discount_or_not (age_client: int, quantity_orders: int, summ_orders: int) -> bool:
    '''
    Магазин предлагает постоянным клиентам и клиентам старше 60 лет скидку.
    Клиент считается постоянным, если он произвел 4 или более заказов общей суммой от
    5000.
    Функция опереляет, получает клиент скидку или нет.

    Аргументы: \\
    age_client(int) - Возраст клиента \\
    quantity_orders(int) - Количество заказов \\
    summ_orders(int) - Сумма заказов

    Возвращает: Информацию, получает клиент скидку или нет.

    '''
    if age_client >= 60:
        return True
    if age_client < 60 and quantity_orders >= 4 and summ_orders >= 5000:
        return True
    return False

def in_size(length: int | float, width: int | float, height: int | float, mass: int | float, distance: int | float) -> bool:
    '''
    Курьерская служба принимает в работу в качестве малогабаритного отправления
    только заказы соответствующие следующим условиям:
    - Сумма длины, ширины и высоты отправления не превышает 150см;
    - Ни одно из измерений не превышает 100см;
    - Масса отправления не превышает 10кг;
    - Расстояние доставки находится в диапазоне от 3 до 10км.

    Функция будет получать от пользователя данные об отправлении и определять, является ли оно малогабаритным.
    
    Аргументы:
    length(int | float) - длина заказа \\
    width(int | float) - ширина заказа \\
    height(int | float) - высота заказа \\
    mass(int | float) - масса заказа \\
    distance(int | float) - расстояние \\
    size(int | float) - размер

    Возвращает: Подходит ли заказ по всем критериям или нет
    '''
    size_sum = length + width + height

    if (size_sum <= 150 and 
        length <= 100 and width <= 100 and height <= 100 and 
        mass <= 10 and 
        distance >= 3 and distance <= 10):
        return True
    return False
    