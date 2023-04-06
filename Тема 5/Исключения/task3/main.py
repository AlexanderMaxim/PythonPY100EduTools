# TODO написать функцию index
from typing import Any

def index(list_: list, value: Any) -> int:
    for idx, cur_value in enumerate(list_):
        if cur_value == value:
            return idx

    raise ValueError("Значение не было найдено")


list_items = [1, 2, "3", 1]
print(index(list_items, 1) == list_items.index(1))  # True
