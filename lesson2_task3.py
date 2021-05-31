# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
seasons_list = ['winter', 'spring', 'summer', 'autumn']
monthes = int(input("Enter a month number: "))

if monthes ==12 or monthes == 1 or monthes == 2:
        print(f"It's {seasons_dict.get(1)}!")
        print(f"It's surely {seasons_list[0]}!")
elif monthes == 3 or monthes == 4 or monthes == 5:
        print(f"It's {seasons_dict.get(2)}!")
        print(f"It's surely {seasons_list[1]}!")
elif monthes == 6 or monthes == 7 or monthes == 8:
        print(f"It's {seasons_dict.get(3)}!")
        print(f"It's surely {seasons_list[2]}!")
elif monthes == 9 or monthes == 10 or monthes == 11:
        print(f"It's {seasons_dict.get(4)}!")
        print(f"It's surely {seasons_list[3]}!")
else:
        print("Wrong number")