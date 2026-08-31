def summ_sell(name_product: list[str]) -> dict[str, int]:

    products = {}

    for i in name_product:
        if i in products:
            products[i] +=1
        else:
            products[i] = 1

    return products

'''
Есть список проданных товаров за день (названия повторяются).

Ввод: список строк (названия товаров).

Вывод: словарь {товар: количество_продаж}.
'''

name_product = ["краска", "кисть", "отвертка", "уровень", "кисть", "кисть", "уровень"]

result = summ_sell(name_product)

for name, sell in result.items():
    print(f"Наименование: {name}, количество: {sell} шт.")
