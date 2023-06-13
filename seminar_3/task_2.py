massage = input("Введите число или строку: ")

if massage.isdigit() and int(massage) >= 0:
    print(int(massage))
elif massage.count(".") == 1 or massage.count("-") == 1:
    print(float(massage))
elif not massage.islower():
    text = massage.lower()
    print(text)
else:
    text = massage.upper()
    print(text)
