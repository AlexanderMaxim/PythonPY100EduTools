from random import randint  # я почитал, но так и не понял, насколько правильно поместить импорт внутри функции?


def get_unique_list_numbers() -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел

    count = 0
    list_ = []

    while count <= 15:
        num = randint(-10, 10)
        if num not in list_:
            list_.append(num)
            count += 1

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
