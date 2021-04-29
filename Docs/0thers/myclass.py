import math as mt

class kwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def oblicz(self, x):
        return self.a*x**2 + self.b*x + self.c

    def rozw(self):
        delta = (self.b)**2 - 4*(self.a*self.c)
        # print(delta)
        if delta > 0:
            rozw1 = (-self.b - mt.sqrt(delta))/(2*self.a)
            rozw2 = (-self.b + mt.sqrt(delta))/(2*self.a)
            print(f'funkcja {self.a}*x^2 + {self.b}*x + {self.c} ma 2 rozwiązania:\n {round(rozw1, 4)}, {round(rozw2, 4)}')
            
        if delta == 0:
            rozw = -self.b/2*self.a
            print(f'funkcja {self.a}*x^2 + {self.b}*x + {self.c} ma 1 rozwiązanie:\n {round(rozw, 4)}')
            
        if delta < 0:
            print(f'funkcja {self.a}*x^2 + {self.b}*x + {self.c} nie ma rzeczywistych rozwiązań')

class zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    
    def wypisz(self):
        if self.im < 0:
            print(f"{self.re}-{self.im}i")
        else:
            print(f"{self.re}+{self.im}i")

    def moduł(self):
        return (self.re**2 + self.im**2)**(1/2)

    @staticmethod
    def dodaj(z1, z2):
        return zespolona(z1.re + z2.re, z1.im + z2.im)

    @staticmethod
    def mnoz(z1, z2):
        return zespolona(z1.re*z2.re - z1.im*z2.im, z1.re*z2.im + z1.im*z2.re)

class ulamek:
    def __init__(self, l, m):
        self.l = l
        self.m = m

    def wypisz(self):
        print(f'{self.l}/{self.m}')

    def skroc_my(self):
        b_temp = self.m
        a_temp = self.l
        while b_temp:
            a_temp, b_temp = b_temp, a_temp%b_temp
        nwd = a_temp
        self.l = self.l/nwd
        self.m = self.m/nwd
        return self.l, self.m

    def skroc(self):
        nwd = mt.gcd(self.l, self.m)
        self.l //= nwd
        self.m //= nwd

    @staticmethod
    def dodaj(x1, x2):
        wynik = ulamek(x1.l*x2.m + x2.l*x1.m, x1.m*x2.m)
        wynik.skroc()
        return wynik



def main():
    print('\n_________________________\nkwadratowa')
    f1 = kwadratowa(2, -4, 2)
    f2 = kwadratowa(1, 4, 3)
    f3 = kwadratowa(2, 1, 2)
    f1.rozw()
    f2.rozw()
    f3.rozw()

    print('\n_________________________\nzespolona')
    z1 = zespolona(5, 2)
    z2 = zespolona(3, -7)
    z_dod = zespolona.dodaj(z1, z2)
    z_mnoz = zespolona.mnoz(z1, z2)
    print(f'suma zesp1 i zesp2 = {z_dod.re} {z_dod.im}i')
    print(f'iloczyn zesp1 i zesp2 = {z_mnoz.re} {z_mnoz.im}i')

    print('\n_________________________\nułamek')
    x1 = ulamek(3, 6)
    x2 = ulamek(5, 7)
    x1.wypisz()
    x2.wypisz()
    print('skrócenie:')
    x1.skroc()
    x1.wypisz()
    print('suma ułamków:')
    x3 = ulamek.dodaj(x1, x2)
    x3.wypisz()


if __name__== '__main__':
    main()