def get_count_char(str_):
    char_dict = {}
    for char in str_.lower():
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1
    return char_dict
def get_char_ratio(dict_):
    total_sum = sum([val for val in dict_.values()])
    char_ratio = {k: round(v / total_sum * 100, 2) for k, v in dict_.items()}
    return char_ratio

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_char_ratio(get_count_char(main_str)))
