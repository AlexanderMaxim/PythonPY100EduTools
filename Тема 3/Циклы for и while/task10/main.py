list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
odd = 0
even = 0

# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

for i in list_:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

# TODO вывести каких чисел больше

if odd > even:
    print("Нечетных чисел больше")
elif odd < even:
    print("Четных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")
