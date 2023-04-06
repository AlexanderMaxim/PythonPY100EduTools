# TODO написать функцию, которая выдает трехзначное число

import random

def rand_num() -> int:
    rand_digit = [random.randint(0, 9) for _ in range(3)]
    str_num = "".join([str(digit) for digit in rand_digit])

    return int(str_num)

print(rand_num())
