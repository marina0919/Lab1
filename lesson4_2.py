wife_name: str = input(f"Как зовут жену?\n")
wife_age: int = int(input(f"Сколько жене лет?\n"))
husband_name: str = str(input(f"Как зовут мужа?\n"))
husband_age: int = int(input(f"Сколько лет мужу?\n"))
wife_age_one_year: int = wife_age + 1
husband_age_one_year: int = husband_age + 1

print(f"""
Эй, жена привет {wife_name}, тебе уже {wife_age} лет,
Через год вам будет {wife_age_one_year}
Эй, муж привет {husband_name}, тебе уже {husband_age} лет
Через год вам будет {husband_age_one_year}
""")

