#-*- coding: utf_8 -*-
from sets import Set

boys = Set(['Adam', 'Bartek', 'Marek'])
girls = Set(['Ewa', 'Marysia'])
teenagers = Set(['Bartek', 'Marek', 'Marysia'])
print 'Adam' in boys
print 'Janina' in girls
girls.add('Janina')
print 'Janina' in girls
teenage_girls = teenagers & girls  # iloczyn zbiorów
mixed = boys | girls  # suma zbiorów
non_teenage_girls = girls - teenage_girls  # ró¿nica zbiorów
print "Dizewczêta nastolatki: ", teenage_girls
print "Wszyscy: ", mixed
print "Kobiety doros³e: ", non_teenage_girls
