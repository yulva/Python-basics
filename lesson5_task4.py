# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

transl = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_task4 = []
with open('task4.txt', 'r') as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        new_task4.append(transl[i[0]] + '  ' + i[1])
    print(new_task4)

with open('task4_2.txt', 'w') as f_obj:
    f_obj.writelines(new_task4)
