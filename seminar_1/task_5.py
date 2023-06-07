from random import randint

rundom_namber = randint(1, 10)
count_try = 0

while count_try < 10:
    x = int(input("Введите число: "))
    if x == rundom_namber:
        print("Вы угадали!")
        break
    elif count_try < 9:
        if x > rundom_namber:
            print("Загаданое число меньше")
        else:
            print("Загаданое число больше")
        count_try += 1
    else:
        print("Не угадали, попробуйте ещё раз")
        break
