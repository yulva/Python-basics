# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_count = int(input("Enter the number of list items:"))
the_list = []
n = 0
l = 0
while n < list_count:
    the_list.append(input("Enter a list item:"))
    n += 1
print("Here is your list: ", the_list)

for m in range(int(len(the_list)/2)):
        the_list[l], the_list[l + 1] = the_list [l + 1], the_list[l]
        l += 2
print("Here is my list: ", the_list)
