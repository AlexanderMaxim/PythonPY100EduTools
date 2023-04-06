# TODO заполнить список случайными числами

import random

start = -100
fin = 100
count = 50
list_ = [random.randint(start, fin) for i in range(count)]

# TODO посчитать количество отрицательных чисел
negative = [num for num in list_ if num < 0]
print(len(negative))
