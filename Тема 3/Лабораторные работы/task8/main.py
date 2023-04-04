money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
increase += 1

while money_capital >= spend:
    money_capital = money_capital + salary - spend
    month += 1
    spend *= increase # Решил, что по аналогии с №4 повышение начинается со 2-го мес

print(month)
