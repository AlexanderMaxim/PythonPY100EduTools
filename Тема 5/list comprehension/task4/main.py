students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

# TODO посчитать средний возраст
ages = [student["age"] for student in students_list]
avg_age = sum(ages) / len(ages)

# TODO распечатать список словарей студентов, возраст которых меньше среднего
print([student for student in students_list if student["age"] < avg_age])
