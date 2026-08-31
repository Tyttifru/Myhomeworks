import random

def products_rand(product_ot: int, product_do: int, how: int) -> set:
    products = []
    for i in range(0,how):
        products.append(random.randint(product_ot, product_do))
    return products

'''
Есть список товаров, которые клиент заказал, и список товаров, которые реально есть на складе.

Ввод: два списка строк (названия товаров).

Вывод: множество товаров из заказа, которых нет на складе (разность).
'''

order_products = set(products_rand(1,51, 15))
stock_products = set(products_rand(1,51, 15))

print (order_products)
print (stock_products)

not_in_stock = order_products.difference(stock_products)
print (not_in_stock) 
