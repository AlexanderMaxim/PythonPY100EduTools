grades_list = [
    5, 2, 5, 2, 4, 4, 5, 5, 5, 2, 4, 2, 4, 3, 4, 4, 5, 5, 4, 2, 3, 5, 3, 5, 2,
    3, 3, 2, 3, 4, 5, 3, 2, 2, 5, 4, 2, 4, 3, 3, 5, 2, 3, 2, 5, 2, 2, 3, 3, 3
]

count = 0  # заводим счетчик для подсчета количества оценок
grade = 5  # искомая оценка

for current_grade in grades_list:  # перебираем все оценки из списка
    if current_grade == grade:
        count += 1
    continue

print(count)
