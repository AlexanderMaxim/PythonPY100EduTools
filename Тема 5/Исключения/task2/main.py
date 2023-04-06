def is_lucky_number(num: int) -> bool:
    if num <= 0: # TODO проверить что число шестизначное и положительное
        raise ValueError("Число не является положительным")
    if len(str(num)) < 6:
        raise ValueError("Число не является шестизначным")

    list_ = [int(digit) for digit in str(num)] # TODO проверить счастливое число или нет
    return sum(list_[:3]) == sum(list_[3:])


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
