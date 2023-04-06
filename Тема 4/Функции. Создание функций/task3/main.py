# TODO запишите здесь функцию factorial
def factorial(n: int):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a


# TODO распечатать результат выполнения функции factorial от числа 5
print(factorial(5))
