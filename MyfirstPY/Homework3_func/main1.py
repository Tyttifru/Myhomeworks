import functions3
import random

reit_list = [random.randint(0, 100) for i in range(1,16)]
print (reit_list)

max_reit = functions3.employee_rating(reit_list)
print(f"Наибольший рейтинг - {max_reit}")