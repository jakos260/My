#-*- coding: utf_8 -*-
from sets import Set

metale_szlachetne = Set()

metale_szlachetne.add('z³oto');
metale_szlachetne.add('srebro')
metale_szlachetne.add('platyna')
metale_szlachetne.add('pallad')
metale_szlachetne.add('osm')
metale_szlachetne.add('rod')
metale_szlachetne.add('iryd')


print 'Metale szlachetne to:'
for metal in Set(metale_szlachetne):
    print metal
