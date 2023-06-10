number = int(input("Введите число: "))

if number < 0:
    print("Введено некоректное число")
elif number == 0:
    print("Введеное число в 2, 8 и строковой системе счисления будет 0")
else:
    print("Введеное число в 2 системе счисления = {0:b}".format(number))
    print("Введеное число в 8 системе счисления = {0:o}".format(number))
    print("Введеное число в строковой системе счисления = {0:x}".format(number), ",", "{0:X}".format(number))
