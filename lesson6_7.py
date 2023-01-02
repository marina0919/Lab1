# В программе имеются изначально следующие 5 строк
# №1 "Вы красавчик"
# №2 "Вы хорошист"
# №3 "Вы среднячок"
# №4 "Вы слабенький"
# №5 "Вы пока еще двоешник"
# №6 "Вы пока еще Чайник"
#
# Программа на вход принимает название двух предметов, например, "Стул" и "Стол"
# Необхнодимо вычислить кол-во символов у входных слов и вывести на экран в зависимости от суммы символов
#
# Если до 3 символов включительно, то стоку №6
# Если от 3 и до 5 символов включительно, то стоку №5
# Если от 5 до 8 символов, то стоку №4
# Если от 8 включительно до 10 символов включительно, то стоку №3
# Если от 10 до 15 символов, то стоку №2
# Если больше 15 символов включительно, то стоку №1
#
#
# !!!
# В задании необходимо использовать только 1 раз print()


item_1: str = str(input("введите предмет 1\n"))
item_2: str = input("введите предмет 2\n")
numbers_1: str = "Вы красавчик"
numbers_2: str = "Вы хорошист"
numbers_3: str = "Вы среднячок"
numbers_4: str = "Вы слабенький"
numbers_5: str = "Вы пока ещё двоешник"
numbers_6: str = "Вы пока ещё чайник"
number_of_characters: int = len(item_1 + item_2)
grade = numbers_1

if number_of_characters <= 3:
    grade = numbers_6
elif (number_of_characters > 3) and (number_of_characters <= 5):
    grade = numbers_5
elif (number_of_characters > 5) and (number_of_characters < 8):
    grade = numbers_4
elif (number_of_characters > 8) and (number_of_characters <= 10):
    grade = numbers_3
elif (number_of_characters > 10) and (number_of_characters < 15):
    grade = numbers_2
elif (number_of_characters >= 15):
    grade = numbers_1

print(f"""
number_of_characters {number_of_characters}
{grade}
""")
