'''
import random

reit_list = []

for i in range (1,16):
    reit_list.append(random.randint(0,100))

print (reit_list)

maxi = reit_list [0]

for i in reit_list:
    if i > maxi:
        i = maxi
print (maxi)
'''

'''
import random

price_zak = []

for i in range (1,21):
    price_zak.append(random.randint(50,150))
print (price_zak)

price_end = []
percent = 18 / 100

for i in price_zak:
    price_end.append(round(i * percent + i, 2))

print (price_end)
'''

'''
import random

man_sales = []

for i in range (0,20):
    man_sales.append(random.randint(1,1000))
print(man_sales)

mans = 0
plan_sales = int(input("Введите план продаж: "))

for i in man_sales:
    if i > plan_sales:
        mans +=1

print(f"Количество сотрудников, выполнившие план: {mans}")
'''

'''
numbers = ["Роман", "Роман", "Юлия", "Юлия", "Софья", "Андрей", "Владимир", "Роман"]
number_end = []

for i in numbers:
    if i not in number_end:
        number_end.append(i)
print(number_end)
print(f"Количество участников: {len(number_end)}")
'''


'''
numbers = ["Роман", "Роман", "Юлия", "Юлия", "Софья", "Андрей", "Владимир"]
x=0

while x < len(numbers):
        if numbers[x] in numbers[:x]:
            numbers.pop(x)
        else:
              x+=1
        
print(numbers)
print(f"Количество участников: {len(numbers)}")
'''






