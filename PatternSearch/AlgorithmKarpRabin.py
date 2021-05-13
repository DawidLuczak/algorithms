def AlgorithmKarpRabin(text, key, q):
    letters = 256
    i, j = 0, 0
    hashT, hashK = 0, 0
    h = 1
    for i in range(len(key) - 1):
        h = (h * letters) % q
    for i in range(len(key)):
        hashK = (letters * hashK + ord(key[i])) % q
        hashT = (letters * hashT + ord(text[i])) % q
    for i in range(len(text) - len(key) + 1):
        if hashT == hashK:
            for j in range(len(key)):
                if text[i + j] != key[j]:
                    break
            j += 1
            if j == len(key):
                return True, i
        if i < len(text) - len(key):
            hashT = (letters * (hashT - ord(text[i]) * h) + ord(text[i + len(key)])) % q
            if hashT < 0:
                hashT = hashT + q


print(AlgorithmKarpRabin("Wyszukiwanie", "nie", 23))
