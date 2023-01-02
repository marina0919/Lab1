my_age = int(input(f"Введи мой возраст?\n"))
if my_age > 18:
    print(f"Поздравляю, ты уже большая девочка")
else:
    print(f"Ты ещё малышка")

if my_age < 3:
    print(f"Дома сиди")
elif (my_age >= 3) and (my_age < 6):
    print(f"Иди в садик")
elif (my_age >= 6) and (my_age < 16):
    print(f"Иди в Школу")
elif (my_age >= 16) and (my_age < 18):
    print(f"Иди в ПТУ")
elif (my_age >= 18) and (my_age < 23):
    print(f"Иди в Универ")
elif (my_age >= 23) and (my_age < 62):
    print(f"Иди работать")
elif my_age >= 62:
    print(f"Иди на пенсию")


