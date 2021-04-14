from math import *


def diff(function, x, dx):
    f_x1 = eval(function)
    x += dx
    f_x2 = eval(function)
    return (f_x2 - f_x1) / dx


def diff2(function, x, dx):
    f_x1 = eval(function)
    x += dx
    f_x2 = eval(function)
    x += dx
    f_x3 = eval(function)
    return (f_x3 - 2 * f_x2 + f_x1) / (dx * dx)


def main(args):
    function = input("Podaj funkcję f(x): ")
    x = float(input("Punkt dla pochodnej funkcji f(x): "))
    dx = float(input("Rozmiar elementarnego przesunięcia: "))

    print("Pochodna funkcji {function} w punkcie {x} dla dx = {dx} jest równa: {diff}".format(function=function, x=x,
                                                                                              dx=dx,
                                                                                              diff=diff(function, x,
                                                                                                        dx)))
    print("Druga pochodna funkcji {function} w punkcie {x} dla dx = {dx} jest równa: {diff2}".format(function=function,
                                                                                                     x=x, dx=dx,
                                                                                                     diff2=diff2(
                                                                                                         function, x,
                                                                                                         dx)))
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))