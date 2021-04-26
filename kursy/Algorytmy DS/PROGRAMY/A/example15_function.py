#-*- coding: utf_8 -*-

import math
import random

def rectangle_perimeter(a, b):
    return 2 * (a + b)
    
def rectangle_area(a, b):
    return a * b    
    
def rectangle_diagonal(a, b):
     return math.sqrt(a*a + b*b)    
     
def dual_rectangle(a, b):
     diag = rectangle_diagonal(a, b)
     res_a = (a*a)/diag
     res_b = (b*b)/diag
     return res_a, res_b      
    
def process_rectangle(a, b):
    print 'Prostok�t o bokach', a, 'i', b, '.'
    print 'Obw�d = ', rectangle_perimeter(a, b)
    print 'Pole = ' , rectangle_area(a, b)
    print 'Przek�tna = ' , rectangle_diagonal(a, b)
    dual_a, dual_b = dual_rectangle(a, b) 
    print 'Boki prostok�ta dualnego:', dual_a, ',', dual_b
    print
    
def random_pair()  :
  return random.randint(1, 99), random.randint(1, 99) 


def process_random_rectangle():
    ga, gb = random_pair()
    process_rectangle(ga, gb)
      


# pocz�tek programu

process_rectangle(2, 3)
process_rectangle(3, 4)

process_random_rectangle()
process_random_rectangle()
process_random_rectangle()

