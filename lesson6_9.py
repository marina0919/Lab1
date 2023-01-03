print(5)
y: int = 5
print(y)
y = y + 1
print(y)
x: int = y
y = y + 1
print(f"1_________")
print(f"x {x}")
x = x + 2
print(f"2_________")
print(f"x {x}")
print(f"y {y}")

z: int = y
y = x
x = z

print(f"3_________")
print(f"x {x}")
print(f"y {y}")

x = x + 1

print(f"4_________")
print(f"x {x}")

x += 1

print(f"5_________")
print(f"x {x}")
