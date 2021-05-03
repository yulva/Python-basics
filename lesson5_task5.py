# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def amount():
    try:
        with open('task5.txt', 'w+') as f_obj:
            line = input('Enter numbers separated by a space: \n')
            f_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('File error!')
    except ValueError:
        print('Input-output error!')


amount()
