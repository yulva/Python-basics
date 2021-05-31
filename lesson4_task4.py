# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

first_list = [1, 5, 7, 9, 4, 6, 8, 6, 4, 2, 7, 5, 3, 1]
second_list = [el for el in first_list if first_list.count(el) == 1]
print(f'The first list is {first_list}')
print(f'The second list is {second_list}')
