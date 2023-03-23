list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение 5-го по порядку элемента средним арифметическим

list_sum = sum(list_numbers)
list_len = len(list_numbers)
list_avg = list_sum / list_len

list_numbers[4] = list_avg

print(list_numbers)
