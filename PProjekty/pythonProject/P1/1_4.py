dict1 = {'a': 5, 'b': 7, 'c': 13}
dict2 = {'c': 15, 'd': 3, 'e': (-5)}
def add_dictionaries(dict1, dict2):
    wynik = {}
    k1 = dict1.keys()
    k2 = dict2.keys()
    for k in dict2:
        if k in wynik:
            wynik[k] = dict1[k] + dict2[k]
        else:
            wynik[k] = dict1[k]
    for k in dict1:
        if k in wynik:
            wynik[k] = dict2[k] + dict1[k]
        else:
            wynik[k] = dict2[k]

    return wynik
dict3 = add_dictionaries(dict1, dict2)
print(dict3)