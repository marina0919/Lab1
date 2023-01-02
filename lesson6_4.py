number_1: int = int(input("Введите первое число\n"))
number_2: int = int(input("Введите второе число\n"))
operation: str = str(input("Введите операцию\n"))
if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    result = number_1 / number_2

else:
    print("операция не реализована")
    exit(0)

print(f"{number_1} {operation} {number_2} = {result}")
print("Успешна завершина")