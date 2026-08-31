cash = int(input("Сумма = "))
age = 18
year = cash * 10 / 100 # за 12 месяцев
mounth = year / 12 # за один месяц
prib = mounth * age
print (f"Сумма вклада = {cash}, прибыль за 18 месяцев при 10% годовых = {prib}")