import functions2

name = input("Введите назввание: ")
price_product = int(input("Введите цену: "))
quantity_product = int(input("Введите количество: "))
in_action = input("Участвует в акции? ")

total_price, action = functions2.action_price (price_product, quantity_product, in_action)

if action > 0:
    print(f"Итого: {name}, {quantity_product} шт, {total_price} руб, скидка {action}%")
else:
    print(f"Итого: {name}, {quantity_product} шт, {total_price} руб, нет скидки")

