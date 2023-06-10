import sys

first_number = input("Введите первую дробь: ")
second_number = input("Введите вторую дробь: ")
index = 0
x1 = ""
x2 = ""
y1 = ""
y2 = ""

while index < len(first_number):
    x1 += first_number[index]
    index += 1
    if first_number[index] == "/":
        index += 1
        while index < len(first_number):
            y1 += first_number[index]
            index += 1

index = 0

while index < len(second_number):
    x2 += second_number[index]
    index += 1
    if second_number[index] == "/":
        index += 1
        while index < len(second_number):
            y2 += second_number[index]
            index += 1

print("Произведение дробей", first_number, "и", second_number, "=", int(x1) * int(x2), "/", int(y1) * int(y2))

if (x1 == y1) & (x2 == y1):
    print("Сумма дробей = 2")
    sys.exit()
elif x1 == y1:
    print("Сумма дробей = ", (int(x2) / int(y2)) + 1)
    sys.exit()
elif x2 == y2:
    print("Сумма дробей = ", (int(x1) / int(y1)) + 1)
    sys.exit()
else:
    print("Сумма дробей = ", ((int(x1) * int(y2)) + (int(y1) * int(x2))) / (int(x2) * int(y2)))
