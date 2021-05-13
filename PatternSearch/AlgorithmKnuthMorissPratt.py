def AlgorithmKnuthMorissPratt(text, key):
    P = helpTable(key)
    i = 0
    while i <= len(text) - len(key):
        j = 0
        while j < len(key) and key[j].lower() == text[i + j].lower():
            j += 1
        if j == len(key):
            return True, i
        i = i + max(1, j - P[j])
    else:
        return False, 0


def helpTable(key):
    P = [0] * len(key)
    i = 0
    for j in range(2, len(key)):
        while i > 0 and key(i + 1) != key[j]:
            i = P[i]
        if key[i + 1] == key[j]:
            i += 1
            P[j] = i
    return P


print(AlgorithmKnuthMorissPratt("Wyszukiwanie", "nie"))