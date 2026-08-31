dlina = float(input("Длина? "))
shir = float(input("Ширина? "))
visota = float(input("Высота? "))
massa = float(input("Масса? "))
trassa = float(input("Расстояние? "))
razmer = dlina + shir + visota

if (dlina + shir + visota) < 150 and dlina < 100 and shir < 100 and visota < 100 and massa > 3 and massa < 10:
    print("Малогабаритный")
else:
    print("Не подходит")
