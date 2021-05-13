def table(text, key):
    table, t = [], []
    for i in range(0, len(text)):
        t.append(text[i])
        if i % key == key - 1:
            table.append(t.copy())
            t.clear()
    while key > len(t) != 0:
        t.append(" ")
    table.append(t.copy())
    return table


def encrypt(table):
    code = ""
    for i in range(len(table[0])):
        for j in range(len(table)):
            code += table[j][i]
    return code


def decrypt(table):
    message = ""
    for i in range(len(table)):
        for j in range(len(table[0])):
            message += table[i][j]
    return message


message = "Abrakadabra"
table = table(message, 3)
code = encrypt(table)
msg = decrypt(table)
for t in table:
    print(t)
print(code)
print(msg)

