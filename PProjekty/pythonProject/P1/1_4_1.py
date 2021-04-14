def add_dictionaries(dict1, dict2):
    wynik = {}
    for key in dict1:
        wynik[key] = dict1[key]
    for key in dict2:
        if key in wynik:
            wynik[key] += dict2[key]
        else:
            wynik[key] = dict2[key]

    return wynik


dict1 = {'a': 5, 'b': 7, 'c': 13}
dict2 = {'c': 15, 'd': 3, 'e': (-5)}
dict3 = add_dictionaries(dict1, dict2)
print(dict3)