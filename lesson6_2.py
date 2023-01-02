my_age = int(input(f"Введи мой возраст?\n"))
# if my_age > 25:
#     salary = 6000
# else:
#     salary = 1000
# print(f"""
# Ваш возраст состовляет {my_age} лет,
# Ваша зп равна {salary} у.e
# """)

salary = 6000 if my_age > 25 else 1000
print(f"""
Ваш возраст состовляет {my_age} лет,
Ваша зп равна {salary} у.e
""")
