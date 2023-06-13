list = [5, "hello", 3.14, True, 5]

for item in set(list):
    count_copi = list.count(item)
    if count_copi > 1:
        for i in range(count_copi):
            list.remove(item)

print(list)
