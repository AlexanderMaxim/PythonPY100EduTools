list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел

unic_nums = set(list_)

sum_ = sum(unic_nums)
len_ = len(unic_nums)

# print(f'Сумма уникальных чисел = {sum_}')
# print(f'Количество уникальных чисел = {len_}')
# print(f'Среднее арифметическое уникальных чисел = {round(sum_ / len_, 5)}')

print(sum_)
print(len_)
print(round(sum_ / len_, 5))
