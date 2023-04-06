def is_palindrome(str_):
    new_str_ = str_.lower().replace(' ', "")  # TODO привести строку к единому регистру и избавиться от пробелов

    if new_str_ == new_str_[::-1]:  # TODO проверка палиндрома
        print("Строка палиндром")
    else:
        print("Строка не палиндром")

is_palindrome("Кит на море не романтик")
is_palindrome("Прочая строка")
