# -*- coding: cp1250 -*-
# Calculation of an error rate for knn algorithms completing the map
# of Italy for the parameters k.

import sys
sys.path.append('../../common')
sys.path.append('..')
import knn  # noqa
import common  # noqa

'italy_100completed_9.pgm'
if len(sys.argv) < 2:
    sys.exit(
        'Podaj nazwę wynikowego obrazu')

completed_image = sys.argv[1]
actual_image = 'italy.pgm'

(completed_img, widthc, heightc, mcolorc) = common.load_pgm_img(
    completed_image)
(actual_img, widtha, heighta, mcolora) = common.load_pgm_img(actual_image)

if widthc != widtha or heightc != heighta:
    raise ValueError('Niezgodne rozmiary obrazów "' + completed_image + '" oraz "' + actual_image + '".')

error_count = 0
for y in range(0, heightc):
    for x in range(0, widthc):
        error_count += int(completed_img[x, y] != actual_img[x, y])

total_pixels = widthc * heightc
error_rate = float(error_count) / total_pixels
print 'Stopa błędu:', error_rate
