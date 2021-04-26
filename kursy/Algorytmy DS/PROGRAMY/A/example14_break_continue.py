#-*- coding: utf_8 -*-

for i in range(0, 10):
    if i % 2 == 1:  # reszta z dzielenia przez 2
        continue
    print 'Liczba', i, 'jest podzielna przez 2.'

for j in range(20, 100):
    print j
    if j * j > 1000:
        print 'Przekroczono wartoœæ graniczn¹', j
        break
print 'Koniec programu'

