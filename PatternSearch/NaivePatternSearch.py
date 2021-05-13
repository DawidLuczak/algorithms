def NaivePatternSearch(string, key):
    k, i = 0, 0
    while i + len(key) - k <= len(string):
        if string[i].lower() == key[k].lower():
            if k == len(key) - 1:
                return True, i - k
            else:
                k += 1
        else:
            k = 0
        i += 1
    else:
        return False, 0


s1 = "Wyszukiwanie"
s2 = "Nie"
result = NaivePatternSearch("Wyszukiwanie", "nie")
print(result)
for i in range(len(s2)):
    print(s1[result[1] + i])