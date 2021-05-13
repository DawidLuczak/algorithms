def CountSort(tab, k):
    P = [0] * k
    for i in range(len(tab)):
        P[tab[i]] += 1
    i = 0
    for j in range(k):
        for l in range(0, P[j]):
            tab[i + l] = j
        i += P[j]


tab = [1, 2, 4, 2, 1, 4, 1, 2, 3, 3]
CountSort(tab, 5)
print(tab)