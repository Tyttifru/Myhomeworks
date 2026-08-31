import functions2

name_client = input("Имя? ")
age_client = int(input("Возраст? "))
quantity_orders = int(input("Количество заказов? "))
summ_orders = int(input("Сумма? "))

if functions2.discount_or_not (age_client, quantity_orders, summ_orders):
    print(f"Поздравляем, {name_client}, вы получаете скидку!")
else:
    print("Скидки нет :(")