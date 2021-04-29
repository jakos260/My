'''
klasy, obiekty, metody, konstruktory... programowanie obiektowe

self - zawsze odnosi się do tej klasy
'''

class planeta: # tworzymy klasę
    def __init__(self, nazwa, inner, rok, R): # definiujemy konstruktor (jak tworzymy obiekt)
        self.nazwa = nazwa
        self.inner = inner
        self.rok = rok
        self.R = R

    def info(self): # metoda nr 1
        if self.inner:
            print(f'{self.nazwa} jest wewnetrzną planetą US, położoną {self.R} AU od Słońca')
        else:
            print(f'{self.nazwa} jest zewnetrzną planetą US, położoną {self.R} AU od Słońca')

    def compare(self): # metoda nr 2
        print(f'rok na planecie {self.nazwa} to ok {round(self.rok / 365, 1)} roku ziemskiego\n')

    def all(self): # metoda nr 3 - wykorzystuje inną metodę
        self.info()
        print(f'rok na tej planecie to ok {round(self.rok / 365, 1)} roku ziemskiego\n')

class Test:
    def __init__(self):
        self.publiczne, self._chronione, self.__prywatne = 1, 2, 3


def main():
    # konstruujemy obiekty
    Mars = planeta('Mars', True, 687, 1.5)
    Jowisz = planeta('Jowisz', False, 4333, 5.2)
    Neptun = planeta('Neptun', False, 60265, 30)

    # wykonujemy ich metody (funkcje)
    Mars.info()
    Mars.compare()
    Jowisz.all()
    Neptun.all()

    # możemy zmienić zmienne obiektu
    Mars.nazwa = 'Wenus'
    Mars.inner = True
    Mars.rok = 243
    Mars.R = 0.7

    Mars.all()

    test = Test()
    print('publiczne', test.publiczne) # publiczny element klasy test
    print('_chronione', test._chronione) # chroniony element, nie wyświetla się w podpowiedziach, musimy wpisać _
    print('__prywatne', test._Test__prywatne) # nie widoczne wgl, odwołanie: _nazwaklasy__nazwaelementu

if __name__ == "__main__":
    main()