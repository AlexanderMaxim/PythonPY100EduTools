list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_num = max(list_numbers)
max_num_idx = list_numbers.index(max_num)

list_numbers[-1], list_numbers[max_num_idx] = list_numbers[max_num_idx], list_numbers[-1]

print(list_numbers)

# # Решение можно сделать более лаконичным? Если не рассматривать вариант с просто "слить строки в одну"?
# idx = list_numbers.index(max(list_numbers))
# list_numbers[-1], list_numbers[idx] = list_numbers[idx], list_numbers[-1]
#
# print(list_numbers)
