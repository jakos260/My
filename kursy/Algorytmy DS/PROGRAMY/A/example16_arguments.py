#-*- coding: utf_8 -*-
# Importowanie biblioteki systemowej w celu operowania na li�cie argument�w
import sys

print
print 'Nazwa programu:', sys.argv[0]

vargs = sys.argv[1:len(sys.argv)]
print 'Argumenty wywo�ania:', vargs
print
