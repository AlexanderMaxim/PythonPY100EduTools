def task(num: int) -> bool:  # TODO добавить аннотацию типов
    return 10 <= sum([int(i) for i in str(num) if i.isdigit()]) <= 99   # TODO найти сумму цифр числа и понять двузначная ли она


print(task(12))
print(task(555))
print(task(-12))
print(task(-149))
