# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def wage():
    try:
        hours, rate, bonus = map(float, argv[1:])
        result = (int(hours) * int(rate)) + int(bonus)
        print(f'Your wage is - {result}')
    except ValueError:
        print('You need to enter three numbers!')


wage()
