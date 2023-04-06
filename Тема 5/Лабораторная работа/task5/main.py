import string
from random import sample

def get_random_password(n: int = 8) -> str:  # TODO написать функцию генерации случайных паролей
    chars = string.ascii_letters + string.digits
    password = "".join(sample(chars, n))

    return password


print(get_random_password())
