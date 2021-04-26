#-*- coding: utf_8 -*-

# Completes the white points in the pgm image using the knn algorithm.
# A white point is replaced by the majority color of the k-closest
# neighbor pooints.

import math
import sys
sys.path.append('../../common')
sys.path.append('..')
import knn  # noqa
import common  # noqa

if len(sys.argv) < 3:
    sys.exit('Prosz� poda� parametry wywo�ania:\n' +
             '1. wej�ciowy plik .pgm,\n' +
             '2. wyj�ciowy plik dla wygenerowanego obrazu,\n' +
             '3. liczba s�siad�w dla algorytmu k-NN.\n\n' +
             'Na przyk�ad:\n' +
             'python knn_to_pgm.py ' +
             'italy_100partial.pgm ' +
             'italy_100completed_3.pgm 3')
input_image = sys.argv[1]
output_image = sys.argv[2]
k = int(sys.argv[3])  # the number of neighbors


def euclidean_metric_2d((x1, y1), (x2, y2)):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


(img_raw, width, height, max_color) = common.load_pgm_img(input_image)
print 'Szeroko��:',width
print 'Wysoko��:',height
print 'Liczba kolor�w:',max_color
# Remove the unclassified instances from the picture.
print 'Usuwam niesklasyfikowane punkty...'
img = {}
for (x, y), color in img_raw.items():
    if int(color) != max_color:
        img[x, y] = color

print 'Konwertuj� ...'
new_img = knn.knn_to_2d_data_with_metric(
    img, 0, width - 1, 0, height - 1, k, euclidean_metric_2d, 10000, max_color)

print 'Renderuj� obraz...'
common.save_pgm_img(output_image, new_img, width, height, max_color)
print 'Sko�czy�em.'