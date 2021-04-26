#-*- coding: utf_8 -*-

# Konstruuje drzewo decyzyjne dla danych zapisanych w pliku CSV
# Format pliku:
# Pierwszy wiersz zawiera nazwy atrybutów oddzielone przecinkami,
# każdy kolejny wiersz zawiera jeden element danych.
# Wartości poszczególnych atrybutów oddzielone są przecinkami
# Ostatni atrybut traktowany jest jako decyzyjny, poprzednie
# są atrybutami warunkującymi.

import math
# Moduł anytree jest używany do wizualizacji drzewa decyzyjnego
# zbudowanego przez niniejszy algorytm

from anytree import Node, RenderTree
import sys
sys.path.append('../common')
import common
from common import printfv
import decision_tree

# Start programu
if len(sys.argv) < 3:
    sys.exit('Proszę podać parametry wywołania:\n' +
              '1. nazwę wejściowego pliku CSV.\n' +
              '2. poziom szczegółowości wyświetlanej informacji:\n' +
              '   0 - tylko drzewo decyzyne,\n' +
              '   1 - drzewo decyzyjne oraz kilka podstawowych informacji,\n' +
              '   2 - drzewo decyzyjne oraz szczegółowe wyjaśnienia.\n\n' +
              'Na przykład:\n' +
              'python construct_decision_tree.py swim.csv 1')
              

csv_file_name = sys.argv[1]
verbose = int(sys.argv[2])  # poziom szczegółowości, 0 - tylko drzewo decyzyjne


# Definicja kolumny zawierającej atrybut decyzyjny
(heading, complete_data, incomplete_data,
 enquired_column) = common.csv_file_to_ordered_data(csv_file_name)

printfv(1, verbose,
        "Konstruowanie drzewa decyzyjnego " +
        "Liczba elementów danych - " +str(len(complete_data)) + "\n" +
        str(complete_data) + "\n\n")

        
tree = decision_tree.construct_decision_tree(
    verbose, heading, complete_data, enquired_column)
printfv(2, verbose, "\n")
printfv(1, verbose, "***Drzewo decyzyjne***\n")
decision_tree.display_tree(tree)
