# TODO реализовать функцию
def get_unique_words(str_):
    list_ = list(set(str_.split()))
    list_.sort()
    return list_

print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
