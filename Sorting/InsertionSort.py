def InsertionSort(tab):
    for i in range(1, len(tab)):
        for j in range(0, i):
            if str(tab[i]) < str(tab[j]):
                tab[j], tab[i] = tab[i], tab[j]


