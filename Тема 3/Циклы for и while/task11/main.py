num = 123
count = 0

# TODO посчитать количество действий над числом согласно условию

while num != 1:
    if num % 2 != 0:
        num = (num * 3 + 1) / 2
        count += 1
    else:
        num /= 2
        count += 1

print(count)
