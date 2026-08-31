name = input("Имя? ")
age = int(input("Возраст? "))
zakaz = int(input("Количество заказов? "))
money = int(input("Сумма? "))

if age >= 60 or age <=60 and zakaz >=4 and money > 5000:
    print(f"Поздравляем, {name}, вы получаете скидку!")
else:
    print("Скидки нет :(")
