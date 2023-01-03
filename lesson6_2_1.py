
age_user: int = int(input("Введите ваш возраст\n"))
the_salary: int =0
if age_user > 25:
    the_salary = 6000
else:
    the_salary = 1000

the_salary = 6000 if age_user > 25 else 1000

print(f""" Ваш возраст состовляет {age_user} лет
Ваша Зп равна {the_salary} y.e""")

























