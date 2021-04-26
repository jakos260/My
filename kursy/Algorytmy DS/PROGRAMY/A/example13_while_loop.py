#-*- coding: utf_8 -*-
a = 37 * 19 * 539
b = -41 * 19 * 113

y = abs(a)
r = abs(b)

while r != 0:
  x = y
  y = r
  r = x % y
  
print 'Najwiêkszy wspólny dzielnik', a , 'i' , b, 'to', y  
