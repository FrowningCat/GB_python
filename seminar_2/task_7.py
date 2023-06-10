number = int(input("Введите число: "))
result = ''

if number < 0:
    print("Введено некоректное число")
elif number == 0:
    print("Введеное число в 16 системе счисления будет 0")
else:
    while number != 0:
        boofer = number
        temp = number % 16 if (number % 16) < 10 else chr(number % 16 + 87)
        result = str(temp) + result
        number //= 16
    result = "0x" + result
    print("Введеное число в 16 системе счисления = {0:x}".format(boofer), "или, в другой записи:", result)
