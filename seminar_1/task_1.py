height = int(input("Введите высоту ёлочки: "))
counter_star = 1
counter_spase = height
height_tree_trunk = 1

if height <= 0:
    print("Введено некоректное число")
else:
    while counter_star <= height * 2:
        spase = " "
        star = "*"
        print(spase * counter_spase, star * counter_star)
        counter_star += 2
        counter_spase -= 1

    while height_tree_trunk <= height:
        counter_spase = height // 2
        tree_trunk = "|"
        if height % 2 == 0:
            print(spase * counter_spase, tree_trunk * (height + 1))
        else:
            print(spase * (counter_spase + 1), tree_trunk * height)
        height_tree_trunk += 2
