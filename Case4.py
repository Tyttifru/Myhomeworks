name = input("Введите назввание ")
sale = int(input("Введите цену "))
how = int(input("Введите количество "))
action = input("Участвует в акции? ")
total = sale * how


if action == "да":
    action = True
else:
    action = False


if how >= 5 and action:
    total = int(total * 75 / 100)
    print (f"Итого:{name}, {how} шт, {total} руб, скидка 25%")
elif how >= 5 and not action:
    total = int(total * 90 / 100)
    print (f"Итого:{name}, {how} шт, {total} руб, скидка 10%")
elif how < 5 and action:
    total = int(total * 85 / 100)
    print (f"Итого:{name}, {how} шт, {total} руб, скидка 15%")
else:
    print (f"Итого:{name}, {how} шт, {total} руб, нет скидки")
    