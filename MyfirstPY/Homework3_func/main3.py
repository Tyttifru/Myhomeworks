import functions3
import random

mans_sales = [random.randint(1,1000) for i in range(0, 20)]
print (mans_sales)

plan_sales = int(input("Введите план продаж: "))

mans = functions3.failed_plan(plan_sales, mans_sales)
print(f"Количество сотрудников, не выполнившие план: {mans}")