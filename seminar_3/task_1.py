array = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 9]

new_list = []
for i in range(len(array)):
    if array[i] not in new_list:
        new_list.append(array[i])
print(new_list)

shot_new_list = list(set(array))
print(shot_new_list)
