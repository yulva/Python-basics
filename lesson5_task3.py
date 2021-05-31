# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("task3.txt", "r") as the_file:
    salary = []
    little_sal = []
    the_list = the_file.read().split("\n")
    for i in the_list:
        i = i.split()
        if int(i[1]) < 20000:
            little_sal.append(i[0])
        salary.append(i[1])
print(f"{little_sal} have salaries less than 20000.\n"
      f"The average salary is {round(sum(map(int, salary)) / len(salary))}.")
