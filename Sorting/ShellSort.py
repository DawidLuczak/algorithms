from math import floor


def ShellSort(tab):
    h = floor(len(tab)/2)
    while h >= 1:
        for i in range(h):
            for j in range(i, len(tab), h):
                for k in range(i, j, h):
                    if str(tab[j]) < str(tab[k]):
                        tab[j], tab[k] = tab[k], tab[j]
        h = floor(h/2)


tab =["b", 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, "h", "a"]
ShellSort(tab)
print(tab)