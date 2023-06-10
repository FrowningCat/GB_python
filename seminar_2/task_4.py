import math
from decimal import Decimal, getcontext

di = float(input("Введите диаметр окружности: "))
getcontext().prec = 42

if di == 0:
    print("Введено некоректное число")
elif di < 0:
    di = abs(di)

C = Decimal(math.pi * di)
S = Decimal((math.pi / 4) * (di ** 2))

print("Длина окружности: ", C)
print("Площадь окружности: ", S)
