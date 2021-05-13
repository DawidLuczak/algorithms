def maximum(data):
    tab = data.split(";")
    top = float('-inf')
    for n in tab:
        try:
            if float(n) > top:
                top = float(n)
        except ValueError:
            continue
    return top


d = "20.52;1;2;5;7;9;-10;10.5;a;"
print(maximum(d))
