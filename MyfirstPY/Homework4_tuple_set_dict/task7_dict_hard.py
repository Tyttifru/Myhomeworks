def average_score_by_department(employees: dict[str, str], scores: list[tuple[str, float]]) -> dict[str, float]:
    
    dept_scores = {}
    
    for employee, score in scores:

        if employee in employees:
            department = employees[employee]
    
            if department not in dept_scores:
                dept_scores[department] = [0, 0]
            
            dept_scores[department][0] += score
            dept_scores[department][1] += 1 
    
    result = {}

    for dept, (total, count) in dept_scores.items():
        result[dept] = round(total / count, 2) if count > 0 else 0
    
    return result

'''
HR хранит данные: {сотрудник: отдел} и отдельно список оценок performance: (сотрудник,
оценка).

Ввод:
1. словарь {name: department},
2. список кортежей (name, score)

Вывод: словарь {department: средняя_оценка_по_отделу} (среднее по тем, у кого есть
оценка).
'''

employees = {"Роман": "frontend", "Сергей": "frontend", "Иван": "support", "Светлана": "frontend"}
scores = [("Роман", 5), ("Сергей", 5), ("Иван", 4), ("Светлана", 3)]

result = average_score_by_department(employees, scores)

print("Средние оценки по отделам:")

for dept, avg in result.items():
    print(f" {dept}: {avg}")


