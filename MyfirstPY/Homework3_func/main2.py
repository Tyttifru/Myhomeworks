import functions3
import random

price_zak = [random.randint(50,150) for i in range (1,21)]
print (f"Стоимость товаров без наценки: {price_zak}")


price_end = functions3.prices_markup(price_zak)
print (f"Стоимость товаров с наценкой: {price_end}")