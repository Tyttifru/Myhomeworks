import random

def courier_coordinates(how_coord: int, max_value: int, min_value: int) -> tuple[int, int]:

   rand_coordinates = []

   for i in range(how_coord):
     x_coord = random.randint(min_value, max_value)
     y_coord = random.randint(min_value, max_value)
     rand_coordinates.append((x_coord, y_coord))
   return rand_coordinates

'''
Курьер за день отмечает точки, где он был: каждая точка — это координаты (x, y).

Ввод: список кортежей (x, y) (целые числа).

Вывод: кортеж с координатами точки, которая находится дальше всего от начала координат
(0,0).
'''

rand_coordinates = tuple(courier_coordinates(5, 10, -10))
print (rand_coordinates)

farthest_distance = rand_coordinates[0]
max_distance = 0

for x, y in rand_coordinates:
    maxis_distance = x**2 + y**2
    if maxis_distance > max_distance:
        max_distance = maxis_distance
        farthest_distance = (x, y)
print(f"Дальше всего от 0,0: {farthest_distance}")
   
  
    
    