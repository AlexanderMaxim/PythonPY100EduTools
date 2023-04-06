# TODO реализовать функцию
def get_sentences_list(str_):
    new_str_ = []
    for i in str_.split("."):
        if i != "":
            new_str_.append(i.strip())
    return new_str_


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
