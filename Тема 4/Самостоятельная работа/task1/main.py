def remove_whitespace(new_str_):
    while True:
        new_str_ = new_str_.replace("  ", " ")
        if "  " not in new_str_:
            break

    return new_str_

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
