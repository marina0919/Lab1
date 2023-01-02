# name = input("Как вас зовут?")
# print("Привет,", name)
# #
# name = input(f"Как вас зовут?\n")
# print(f"Привет, {name}")
# #
# name = input("Как вас зовут?\n")
# husband_name = input("Как зовут вашего мужа?\n")
# print(f"""Привет,{name}
# и Привет вашему мужу {husband_name}""")
# #
wife_name = input(f"Как зовут жену?\n")
wife_age: int = int(input(f"{wife_name}, cколько вам лет?\n"))
husband_name: str = str(input(f"Как зовут мужа?\n"))
husband_age: int = int(input(f"Сколько лет мужу?\n"))
print(f"""
Эй, жена привет {wife_name}, тебе уже {wife_age} лет,
Через год вам будет {wife_age+1}
Эй, муж привет {husband_name}, тебе уже {husband_age} лет
Через год вам будет {husband_age+1}
""")
