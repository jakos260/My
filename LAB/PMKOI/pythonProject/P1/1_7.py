
def func7(arg):
    dict = {}
    lista = list(arg)
    for i in range(1, len(lista)+1):
        l_p = []
        for j in range(1, len(lista)+1):
            if(i != j):
                l_p.append(j)
        k_p = tuple(l_p)
        dict[i] = k_p
    return dict
krotka = (1, 2, 3, 4, 5)
print(func7(krotka))