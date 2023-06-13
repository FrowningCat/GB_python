tuple = (5, "hello", 3.14, True, 3)
dictionary = {}

for i in tuple:
        dictionary.setdefault(type(i), []).append(i)

print(dictionary)