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

class Licznik:
    ile = 0 # pole statyczne (stworzone poza kostruktorem)
    def __init__(self):
        Licznik.ile += 1
        self.ktory = Licznik.ile
        print(f'to jest obiekt nr{Licznik.ile}')
        
    def __del__(self):
        Licznik.ile -= 1
        print(f'usunięto obiekt {self.ktory}, pozostało jeszcze {Licznik.ile} obiektów')

    @staticmethod # dekorator (tak oznaczamy metodę statyczną po prostu)
    def policz(): # metoda statyczna
        return Licznik.ile

def main():
    # # konstruujemy obiekty
    # Mars = planeta('Mars', True, 687, 1.5)
    # Jowisz = planeta('Jowisz', False, 4333, 5.2)
    # Neptun = planeta('Neptun', False, 60265, 30)

    # # wykonujemy ich metody (funkcje)
    # Mars.info()
    # Mars.compare()
    # Jowisz.all()
    # Neptun.all()

    # # możemy zmienić zmienne obiektu
    # Mars.nazwa = 'Wenus'
    # Mars.inner = True
    # Mars.rok = 243
    # Mars.R = 0.7

    # Mars.all()

    # test = Test()
    # print('publiczne', test.publiczne) # publiczny element klasy test
    # print('_chronione', test._chronione) # chroniony element, nie wyświetla się w podpowiedziach, musimy wpisać _nazwaelementu
    # print('__prywatne', test._Test__prywatne) # nie widoczne wgl, odwołanie: _nazwaklasy__nazwaelementu

    # konstruowanie obiektów
    a = Licznik()
    b = Licznik()
    c = Licznik()
    # zwracanie numerów obiektów
    print(f"a to obiekt nr {a.ktory}") # obiekt
    print(f"b to obiekt nr {b.ktory}")
    print(f"c to obiekt nr {c.ktory}")
    # usuwanie obiektów
    print(f"Liczba obiektow to: {Licznik.policz()}") # pole statyczne (odwołujemy się nie przez obiekt, a przez nazwę klasy)
    a = None
    b = None
    print(f"Liczba obiektow to: {Licznik.policz()}")

if __name__ == "__main__":
    main()