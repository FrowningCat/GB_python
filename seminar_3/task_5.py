list = [1, 2, 3, 3, 4, 5, 6, 6, 7]
new_list = []

for item, i in enumerate(list, start=1):
    if i % 2:
        new_list.append(item)

print(new_list)
