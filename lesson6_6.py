name_user: str = str(input("Имя пользователя\n"))
result: int = len(name_user)
if result <= 3:
    print(f"У вас короткое имя, которое имеет длинну:{result} букв")
elif result == 4:
    print(f"У вас средней длинны имя, которое имеет длинну:{result} букв")
elif result >= 5:
    print(f"у вас длинное имя, которое имеет длинну:{result} букв")

user_last_name: str = str(input("Фамилия пользователя\n"))
result_last_name: int = len(user_last_name)
if result_last_name <= 3:
    print(f"У вас короткая фамилтя, которое имеет длинну:{result_last_name} букв")
elif result_last_name == 4:
    print(f"У вас средней длинны фамилия, которое имеет длинну:{result_last_name} букв")
elif result_last_name >= 5:
    print(f"у вас длинная фамилия, которое имеет длинну:{result_last_name} букв")

user_age: int = int(input("Возраст пользователя\n"))
the_salary: int = 0
if user_age > 18:
    the_salary = (user_age * result) + (user_age * result_last_name)
elif user_age > 16:
    the_salary = user_age * result
elif user_age > 10:
    the_salary = result_last_name + result


tax_the_salary: float = the_salary / 100 * 20
the_rest_of_the_salary: float = the_salary - tax_the_salary

print(f"""Зарплата {the_salary} у.е
Налог {tax_the_salary} у.e
Остаток ЗП {the_rest_of_the_salary} y.e 
""")



