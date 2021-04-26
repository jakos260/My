#-*- coding: utf_8 -*-
from sets import Set

boys = Set(['Adam', 'Bartek', 'Marek'])
girls = Set(['Ewa', 'Marysia'])
teenagers = Set(['Bartek', 'Marek', 'Marysia'])
print 'Adam' in boys
print 'Janina' in girls
girls.add('Janina')
print 'Janina' in girls
teenage_girls = teenagers & girls  # iloczyn zbior�w
mixed = boys | girls  # suma zbior�w
non_teenage_girls = girls - teenage_girls  # r�nica zbior�w
print "Dizewcz�ta nastolatki: ", teenage_girls
print "Wszyscy: ", mixed
print "Kobiety doros�e: ", non_teenage_girls
