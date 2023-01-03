age_users: int = int(input("Введите возраст\n"))
go: str = ""
if 3 <= age_users <= 5:
    go = "иди в садик"
elif 6 <= age_users <= 16:
    go = "иди в школу"
elif 17 <= age_users <= 21:
    go = "иди в универ"
elif 21 <= age_users <= 65:
    go = "иди работай"

long: int = len(go)
text: str = f"""ваш возраст {age_users} лет
{go}
длинна строки {long} символов"""

print(text)

print_length: int = len(text)
print(f"длинна принта {print_length}")
