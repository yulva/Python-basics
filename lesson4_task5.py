# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def the_list(a_1, a_2):
    return a_1 * a_2


print(f'List of even values: {[a for a in range(100, 1001, 2) if a % 2 == 0]}')
print(f'The result of the multiplication of all the elements of the list - {reduce(the_list, [a for a in range(100, 1001, 2) if a % 2 == 0])}')
