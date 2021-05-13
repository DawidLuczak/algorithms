def AlgorithmBoyerMoore(text, key):
    i = len(key) - 1
    while i < len(text):
        j = 0
        while j < len(key) and text[i - j] == key[len(key) - 1 - j]:
            j += 1
        if j == len(key):
            return True, i - j + 1
        i += 1
    else:
        return False, 0


print(AlgorithmBoyerMoore("Wyszukiwanie", "nie"))
