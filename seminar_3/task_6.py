massage = input("Введите строку: ")
words = massage.split()
max_length = len(words[0])
for i in words:
    if len(i) > max_length:
        max_length = len(i)

words.sort()

for number, line in enumerate(words, start=1):
    print(f"{number} {line:>{max_length}}")
