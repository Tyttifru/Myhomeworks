def calculate_total(receipt: list[tuple[str, int, int]]) -> int:

    total_price = 0

    for name_product, how_product, price_product in receipt:
        total_price += how_product * price_product

    return total_price

'''
Касса выдала чек как список позиций: (название_товара, количество, цена за штуку).

Ввод: список кортежей (str, int, int)

Вывод: общая сумма чека
'''

receipt = [
    ("Сыр", 2, 250),
    ("Макароны", 3, 80),
    ("Кофе", 1, 300),
    ("Чай", 1, 150)
]

total_price = calculate_total(receipt)

print(f"Чек:")
for name_product, how_product, price_product in receipt:
    print(f"{name_product}: {how_product} x {price_product} = {how_product * price_product} руб.")
print(f"Общая сумма чека: {total_price} руб.")