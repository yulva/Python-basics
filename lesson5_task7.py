# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('task7_2.json', 'w', encoding='utf-8') as the_file:
    with open('task7.txt', encoding='utf-8') as f_obj:
        earnings = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        total = [earnings, {"average earnings": round(sum([int(i) for i in earnings.values() if int(i) > 0]) /
                                                      len([int(i) for i in earnings.values() if int(i) > 0]))}]
    json.dump(total, the_file, ensure_ascii=False, indent=4)
