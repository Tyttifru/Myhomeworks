def get_best_manager(list_of_deals: dict[str, int]) -> str:

    if not list_of_deals:
       return None
    
    best_manager = None
    max_sell = 0

    for manager, sales in list_of_deals.items():
     if sales > max_sell:
        max_sell = sales
        best_manager = manager
    return best_manager

'''

Есть список сделок: (manager, amount). Нужно понять, кто принёс больше всего денег.

Ввод: список кортежей (str, int/float).

Вывод: имя менеджера с максимальной суммой продаж (если несколько — любой из них или по
алфавиту, уточни правило)
'''

list_of_deals = ({"Роман": 500, "Юлия": 1000, "Софья": 1500})
result = get_best_manager(list_of_deals)

print(result)







