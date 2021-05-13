def BubbleSort(tab):
    for i in range(len(tab) - 1, 1, -1):
        for j in range(0, i):
            if str(tab[i]) < str(tab[j]):
                tab[i], tab[j] = tab[j], tab[i]


tab = ["b", 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, "h", "a"]
BubbleSort(tab)
print(tab)