age_user: int = int(input("Возраст пользователя\n"))
salary_user: int = 0
pensiya_user: int = 0
if (age_user > 18) and (age_user < 60):
    salary_user = 6000
elif age_user >= 60:
    pensiya_user = 2000
elif age_user <= 15:
    salary_user = 0
else:
    salary_user = 1000

# print(f"""Его\nзп = {salary_user} y.e
# пенсия = {pensiya_user} BYN""")

if salary_user > 0:
    print(f"Его зарплата - {salary_user}")

if pensiya_user > 0:
    print(f"Его пенсия - {pensiya_user}")
