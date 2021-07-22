from tkinter import *


# tworzymy funkcję odpowiadającą za dodawanie liczb
def wynikDodawania():
    # pobieramy wartość pierwszego pola metodą .get()
    etykietaPierwszaliczba = polePierwszejLiczby.get()

    # konwertujemy tekstową wartość pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaPierwszaLiczba = float(etykietaPierwszaliczba)

    # pobieramy wartość drugiego pola metodą .get()
    etykietaDrugiejLiczby = poleDrugiejLiczby.get()

    # konwertujemy tekstową wartość pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaDrugiejLiczby = float(etykietaDrugiejLiczby)

    # tworzymy definicję funkcji wywołania dodawania
    wynik = danaPierwszaLiczba + danaDrugiejLiczby
    etykietaWynik.config(text=str(wynik))


# tworzymy funkcję odpowiadającą za odejmowanie liczb
def wynikOdejmowania():
    # pobieramy wartość pierwszego pola metodą .get()
    etykietaPierwszaliczba = polePierwszejLiczby.get()

    # konwertujemy wartość tekstową pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaPierwszaLiczba = float(etykietaPierwszaliczba)

    # pobieramy wartość drugiego pola metodą .get()
    etykietaDrugiejLiczby = poleDrugiejLiczby.get()

    # konwertujemy tekstową wartość pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaDrugiejLiczby = float(etykietaDrugiejLiczby)

    # tworzymy definicję funkcji wywołania odejmowania
    wynik = danaPierwszaLiczba - danaDrugiejLiczby
    etykietaWynik.config(text=str(wynik))


# tworzymy funkcję odpowiadającą za mnożenie
def wynikMnozenia():
    # pobieramy wartość pierwszego pola metodą .get()
    etykietaPierwszaliczba = polePierwszejLiczby.get()

    # konwertujemy wartość tekstową pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaPierwszaLiczba = float(etykietaPierwszaliczba)

    # pobieramy wartość drugiego pola metodą .get()
    etykietaDrugiejLiczby = poleDrugiejLiczby.get()

    # konwertujemy tekstową wartość pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaDrugiejLiczby = float(etykietaDrugiejLiczby)

    # tworzymy definicję funkcji wywołania mnożenia
    wynik = danaPierwszaLiczba * danaDrugiejLiczby
    etykietaWynik.config(text=str(wynik))


# tworzymy funkcję odpowiadającą za dzielenie
def wynikDzielenia():
    # pobieramy wartość pierwszego pola metodą .get()
    etykietaPierwszaliczba = polePierwszejLiczby.get()

    # konwertujemy wartość tekstową pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaPierwszaLiczba = float(etykietaPierwszaliczba)

    # pobieramy wartość drugiego pola metodą .get()
    etykietaDrugiejLiczby = poleDrugiejLiczby.get()

    # konwertujemy tekstową wartość pierwszego pola na liczbę zmiennoprzecinkową typu float
    danaDrugiejLiczby = float(etykietaDrugiejLiczby)

    # tworzymy definicję funkcji wywołania dzielenia
    wynik = danaPierwszaLiczba / danaDrugiejLiczby
    etykietaWynik.config(text=str(wynik))


# tworzymy okno ekranu głównego
ekranGlowny = Tk()

# nadajemy nazwę okna głównego "Kalkulator"
ekranGlowny.title('Kalkulator')

# blokujemy możliwość zmiany rozmiaru ekranu głównego
ekranGlowny.resizable(width=False, height=False)

# tworzymy etykietę pierwszej liczby
etykietaPierwszaliczba = Label(ekranGlowny, text='Wpisz pierszą liczbę: ')
etykietaPierwszaliczba.grid(sticky=W, padx=5, pady=5, row=0, column=0)

# tworzymy pole pierwszej liczby
polePierwszejLiczby = Entry(ekranGlowny, width=20)
polePierwszejLiczby.grid(sticky=W, padx=5, pady=5, row=0, column=1)

# tworzymy etykietę drugiej liczby
etykietaDrugiejLiczby = Label(ekranGlowny, text='Wpisz drugą liczbę: ')
etykietaDrugiejLiczby.grid(sticky=W, padx=5, pady=5, row=1, column=0)

# tworzymy pole drugiej liczby
poleDrugiejLiczby = Entry(ekranGlowny, width=20)
poleDrugiejLiczby.grid(sticky=W, padx=5, pady=5, row=1, column=1)

# tworzymy etykietę wynik
etykietaWynik = Label(ekranGlowny, text='wynik')
etykietaWynik.grid(sticky=E + W, padx=5, pady=5, row=2, column=0, columnspan=2)

# tworzymy przycisk dodawania
przyciskDodawanie = Button(ekranGlowny, text='+', command=wynikDodawania)
przyciskDodawanie.grid(sticky=E + W, padx=5, pady=5, row=3, column=0)

# tworzymy przycisk odejmowania
przyciskOdejmowania = Button(ekranGlowny, text='-', command=wynikOdejmowania)
przyciskOdejmowania.grid(sticky=E + W, padx=5, pady=5, row=3, column=1)

# tworzymy przycisk mnożenia
przyciskMnozenia = Button(ekranGlowny, text='*', command=wynikMnozenia)
przyciskMnozenia.grid(sticky=E + W, padx=5, pady=5, row=4, column=0)

# tworzymy przycisk dzielenia
przyciskDzielenia = Button(ekranGlowny, text='/', command=wynikDzielenia)
przyciskDzielenia.grid(sticky=E + W, padx=5, pady=5, row=4, column=1)

ekranGlowny.mainloop()