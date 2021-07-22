#-*- coding: utf_8 -*-
import math

point_a = (1.2, 2.5)
point_b = (5.7, 4.8)

# funkcja  math.sqrt oblicza pierwiastek kwadratowy z liczby rzeczywistej.
# funkcja math.pow oblicza warto�� pot�gi.

segment_length = math.sqrt(
    math.pow(point_a[0] - point_b[0], 2) +
    math.pow(point_a[1] - point_b[1], 2))
    
print "Wsp�rz�dne punktu A wynosz�", point_a, "cm."
print "Wsp�rz�dne punktu B wynosz�", point_b, "cm."
print "Odleg�o�� mi�dzy punktami A i B wynosi", segment_length, "cm."
