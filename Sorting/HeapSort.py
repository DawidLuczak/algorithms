def heapify(tab, i, m):
    l = 2 * i
    r = 2 * i + 1
    if l < m and str(tab[i]) < str(tab[l]):
        max = l
    else:
        max = i
    if r < m and str(tab[max]) < str(tab[r]):
        max = r
    if max != i:
        tab[i], tab[max] = tab[max], tab[i]
        heapify(tab, max, m)


def heapSort(tab):
    n = len(tab)
    for i in range(int(n/2), -1, -1):
        heapify(tab, i, n)
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, 0, i)



tab = ["b", 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, "h", "a"]
heapSort(tab)
print(tab)