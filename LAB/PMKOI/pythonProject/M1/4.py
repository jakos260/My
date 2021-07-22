x = input()
x = int(x)

def pow(x):
    i = 0
    wynik = 1
    while i < x:
        i += 1
        wynik = wynik*i
    return wynik

print(x,'silnia to: ',pow(x))
