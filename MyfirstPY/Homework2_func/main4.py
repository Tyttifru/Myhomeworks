import functions2

length = float(input("Длина? "))
width = float(input("Ширина? "))
height = float(input("Высота? "))
mass = float(input("Масса? "))
distance = float(input("Расстояние? "))

size = length + width + height

print(f"Длина = {length}, Ширина = {width}, Высота = {height}, Размер = {size}")
print(f"Масса = {mass}, Расстояние = {distance}")

if functions2.in_size(length, width, height, mass, distance):
    print("Малогабаритный, подходит")
else:
    print("Крупногабаритный, не подходит!")