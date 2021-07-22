#-*- coding: utf_8 -*-
# Importowanie biblioteki systemowej w celu operowania na liœcie argumentów
import sys

print
print 'Nazwa programu:', sys.argv[0]

vargs = sys.argv[1:len(sys.argv)]
print 'Argumenty wywo³ania:', vargs
print
