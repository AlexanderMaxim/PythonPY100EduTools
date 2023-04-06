students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

# TODO распечатать с использованием f-строк
for name, res in students_dict.items():
    print(f"Студент {name} получил {res} баллов")
