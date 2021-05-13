def QuickSort(tab, left, right):
    if len(tab) == 1:
        return tab
    if left < right:
        pivot = left
        for i in range(left, right):
            if str(tab[i]) <= str(tab[right]):
                tab[i], tab[pivot] = tab[pivot], tab[i]
                pivot += 1
        tab[pivot], tab[right] = tab[right], tab[pivot]
        QuickSort(tab, left, pivot - 1)
        QuickSort(tab, pivot + 1, right)


tab = ["b", 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, "h", "a"]
QuickSort(tab, 0, len(tab) - 1)
print(tab)