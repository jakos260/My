#-*- coding: utf_8 -*-
# Zapis do pliku "test.txt"
file = open("test.txt", "w")
file.write("pierwszy wiersz\n")
file.write("drugi wiersz")
file.close()

# Odczyt z pliku
file = open("test.txt", "r")
print file.read()
