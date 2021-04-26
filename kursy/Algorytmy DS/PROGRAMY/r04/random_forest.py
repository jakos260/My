#-*- coding: utf_8 -*-

import math
import random
import sys
sys.path.append('../common')
import common  # noqa
import decision_tree  # noqa
from common import printfv  # noqa


# Losowanie próby cech
def sample_with_replacement(population, size):
    sample = []
    for i in range(0, size):
        sample.append(population[random.randint(0, len(population) - 1)])
    return sample


def construct_random_forest(verbose, heading, complete_data,
                            enquired_column, m, tree_count):
    printfv(2, verbose, "*** Konstruowanie lasu losowego ***\n")
            
    printfv(2, verbose, "Konstruowanie lasu losowego składającego się " +
            "z %d losowych drzew decyzyjnych.\n", tree_count)
            
    random_forest = []
    for i in range(0, tree_count):
        printfv(2, verbose, "\nBudowanie losowego drzewa decyzyjnego nr %d:\n", i)
                
        random_forest.append(construct_random_decision_tree(
            verbose, heading, complete_data, enquired_column, m))

            
    printfv(2, verbose, "\nZakończono konstruowanie lasu losowego " +
            "składającego się z %d " +
            "losowych drzew decyzyjnych.\n", tree_count)
            
    return random_forest


#def construct_random_decision_tree(verbose, heading, complete_data,
#                                   enquired_column, m):
#    sample = sample_with_replacement(complete_data, len(complete_data))
#    printfv(2, verbose, "We are given %d features as the input data. " +
#            "Out of these, we choose randomly %d features with the " +
#            "replacement that we will use for the construction of " +
#            "this particular random decision tree:\n" +
#            str(sample) + "\n", len(complete_data),
#            len(complete_data))
#    return decision_tree.construct_general_tree(verbose, heading,
#                                                sample,
#                                                enquired_column, m)
                                                
def construct_random_decision_tree(verbose, heading, complete_data,
                                   enquired_column, m):
    sample = sample_with_replacement(complete_data, len(complete_data))
    printfv(2, verbose, "Dane wejściowe  obejmują %d cech, " +
            "spośród których losujemy ze zwracaniem %d w celu zbudwania niniejszego " +
            "losowego drzewa decyzyjnego: \n" +
            str(sample) + "\n", len(complete_data),
            len(complete_data))
            
            
    return decision_tree.construct_general_tree(verbose, heading,
                                                sample,
                                                enquired_column, m)
                                                


def display_forest(verbose, forest):
    if verbose > 0:
        print "\n*** Graf lasu losowego ***"
        for i in range(0, len(forest)):
            print "\nDrzewo nr " + str(i) + ":"
            decision_tree.display_tree(forest[i])

# M jest liczbą zmiennych, czyli właściwości każdej cechy

def choose_m(verbose, M):
    m = int(min(M, math.ceil(2 * math.sqrt(M))))
            
    printfv(2, verbose, "Mamy M=" + str(M) +
            " zmiennych służących do klasyfikowania cech. ")
            
    printfv(3, verbose, "Algorytm budowania lasu losowego zwykle nie wykorzystuje " +
            "wszystkich zmiennych do wyprowadzania rozgałęzień z węzłów. ")
            
    printfv(3, verbose, "W tym przypadku ograniczamy się do " + str(m) + ". ")
    
    printfv(3, verbose, "Im większa wartość m, tym silniejszy klasyfikator, "  +
            "jednocześnie jednak większa podatność na polaryzację " +
            "przy zwiększaniu liczebności danych wejściowych. " +
            "Lepszym rozwiązaniem jest konstruowanie większej liczby drzew " + 
            "decyzyjnych opartych na słabych klasyfikatorach, bowiem ich " +
            "kombinacja daje wyniki porównywalne z silnym klasyfikatorem." +
            "W celu wyeliminowania polaryzacji z lasu wynikowego powinniśmy " +
            "przyjmować wartość m nieco mniejszą niż M. \n")
            
    printfv(2, verbose, "Zalecaną wartością m jest "
            "m=min(M,math.ceil(2*math.sqrt(M)))" +
            "=min(M,math.ceil(2*math.sqrt(%d)))=%d.\n", M, m)
    return m


def display_classification(verbose, random_forest, heading,
                           enquired_column, incomplete_data):
    printfv(0, verbose, "\n *** Klasyfikacja ***\n\n")
            
    printfv(3, verbose, "Ponieważ do konstrukcji losowego drzewa decyzyjnego" +
            " wykorzystujemy jedynie podzbiór oryginalnych danych,\n" +
            " możemy nie dysponować zbiorem cech wystarczającym do zbudowania pełnego drzewa" +
            " zdolnego do klasyfikowania każdej cechy.\n W takim przypadku" +
            " drzewo nie zwróci żadnej klasy dla konkretnej " +
            "cechy i nie będzie uwzględniane w końcowym głosowaniu.\n\n")
            
            
    if len(incomplete_data) == 0:
        printfv(0, verbose, "Brak danych do klasyfikowania.\n")
    else:
        for incomplete_feature in incomplete_data:
            printfv(0, verbose, "\nCecha: " +
                    str(incomplete_feature) + "\n")
            display_classification_for_feature(
                verbose, random_forest, heading,
                enquired_column, incomplete_feature)


def display_classification_for_feature(verbose, random_forest, heading,
                                       enquired_column, feature):
    classification = {}
    for i in range(0, len(random_forest)):
        group = decision_tree.classify_by_tree(
            random_forest[i], heading, enquired_column, feature)
        common.dic_inc(classification, group)
        
        
        # A. Grazynski
                
        if group is None:
           werdykt = "wstrzymuje się od głosu"
        else:
           werdykt = "głosuje na klasę '" + group + "'"

        printfv(0, verbose, "Drzewo nr " + str(i) + " " + werdykt + "\n")
 # ------------                     
                
    printfv(0, verbose, "Klasa o największej liczbie głosów to " +
            "'" + str(common.dic_key_max_count(classification)) + "',\n" + 
            "zatem cecha " + str(feature) + " zostaje zaliczona " +
            "przez las losowy do klasy '" +
            str(common.dic_key_max_count(classification)) + "'.\n")

# Start programu
if len(sys.argv) < 4:
    sys.exit('Please, input as arguments:\n' +
             '1. the name of the input CSV file,\n' +
             '2. the number of the trees in the random forest to be ' +
             'constructed,\n' +
             '3. output verbosity level:\n' +
             '\t0 for the least output - result of the classification,\n' +
             '\t1 includes in addition the output of the trees constructed ' +
             'and the result of the classification,\n' +
             '\t2 includes in addition brief explanations of the tree ' +
             'construction and classification,\n' +
             '\t3 includes detailed explanations of the algorithm.\n')

csv_file_name = sys.argv[1]
tree_count = int(sys.argv[2])
verbose = int(sys.argv[3])

(heading, complete_data, incomplete_data,
 enquired_column) = common.csv_file_to_ordered_data(csv_file_name)
m = choose_m(verbose, len(heading))
printfv(2, verbose, "We are given the following features:\n" +
        str(complete_data) + "\n When constructing a random " +
        "decision tree as a part of a random forest, we will choose " +
        "only a subset out of them in a random way with the " +
        "replacement.\n\n")

random_forest = construct_random_forest(
    verbose, heading, complete_data, enquired_column, m, tree_count)
display_forest(verbose, random_forest)
printfv(2, verbose, "\n")
printfv(0, verbose, "Liczba drzew w lesie losowym: %d.\n",
        len(random_forest))
printfv(0, verbose, "Makymalna liczba zmiennych uwzglednianych w węźle: %d.\n", m)
display_classification(verbose, random_forest, heading,
                       enquired_column, incomplete_data)
