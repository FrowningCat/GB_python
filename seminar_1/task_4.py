namber = int(input("Введите число: "))
res = 0
x = 1

if namber > 100000:
    print("Введено слишком большое число")
elif namber < 0:
    namber = abs(namber)

while x <= namber:
    if namber % x == 0:
        res += 1
    x += 1

if res > 2:
    print("Число cоставное")
else:
    print("Число простое")
