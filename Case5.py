table = int(input("Введите количество гостей: "))
if table <= 2:
    print("Маленький стол")
elif table <=4:
    print("Cредний стол")
elif table <=8:
    print("Большой стол")
else:
    print ("Гуляй, Вуася")