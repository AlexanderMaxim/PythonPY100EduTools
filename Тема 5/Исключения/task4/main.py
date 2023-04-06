# TODO написать функцию remove
from typing import Any

def remove(list_: list, value: Any) -> list:
    for idx, cur_value in enumerate(list_):
        if cur_value == value:
            return list_[:idx] + list_[idx+1:]

    raise ValueError("Значение не найдено")


print(remove([0, 0, 1, 2], 0))  # [0, 1]
print(remove([0, 1, 1, 2, 3], 1))  # [0, 1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
