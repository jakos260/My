#-*- coding: utf_8 -*-


# Program odczytuje zawartość pliku danych CSV i oblicza wartość 
# bayesowkiego prawdopodobieństwa oznaczoną pierwotnie przez znak zapytania

# Pierwszy wiersz pliku wejściowego ma specjalne znaczenie - jest nagłówkiem
# zawierającym nazwy kolumn oddzielone przecinkami.
# Każdy kolejny wiersz zawiera wartości elementów danych oddzielone przecinkami.
# Dopuszcza się, by wiersz zawierał w ostatniej kolumnie znak zapytania,
# oznaczający wartość, którą trzeba obliczyć.
# Przykładowy plik wejściowy nosi nazwę chess.csv, a polecenie uruchamiające
# program ma postać
#
#    $ python naive_bayes.py chess.csv


import imp
import sys
sys.path.append('../common')
import common  # noqa


# Obliczenie prawdopodobieństwa bayesowskiego dla wierszy z niekompletnymi danymi
# i zwrócenie tych wierszy w kompletnej postaci. Podstawę obliczeń stanowią dane 
# z kompletnych wierszy.



def bayes_probability(heading, complete_data, incomplete_data,
                      enquired_column):
    conditional_counts = {}
    enquired_column_classes = {}
    for data_item in complete_data:
        common.dic_inc(enquired_column_classes,
                       data_item[enquired_column])
        for i in range(0, len(heading)):
            if i != enquired_column:
                common.dic_inc(
                    conditional_counts, (
                        heading[i], data_item[i],
                        data_item[enquired_column]))

    completed_items = []
    for incomplete_item in incomplete_data:
        partial_probs = {}
        complete_probs = {}
        probs_sum = 0
        for enquired_group in enquired_column_classes.items():
            
            # Dla każdej klasy zmiennej A obliczane jest prawdopodobieństwo
            # P(A)*P(B1|A)*P(B2|A)*...*P(Bn|A), gdzie B1,...,Bn są pozostałymi 
            # zmiennymi
            
            probability = float(common.dic_key_count(
                enquired_column_classes,
                enquired_group[0])) / len(complete_data)
            for i in range(0, len(heading)):
                if i != enquired_column:
                    probability = probability * (float(
                        common.dic_key_count(
                            conditional_counts, (
                                heading[i], incomplete_item[i],
                                enquired_group[0]))) / (
                        common.dic_key_count(enquired_column_classes,
                                             enquired_group[0])))
            partial_probs[enquired_group[0]] = probability
            probs_sum += probability

        for enquired_group in enquired_column_classes.items():
            complete_probs[enquired_group[0]
                           ] = partial_probs[enquired_group[0]
                                             ] / probs_sum
        incomplete_item[enquired_column] = complete_probs
        completed_items.append(incomplete_item)
    return completed_items

# Początek programu
if len(sys.argv) < 2:
    sys.exit('Proszę podać nazwę wejściowego pliku CSV')

(heading, complete_data, incomplete_data,
 enquired_column) = common.csv_file_to_ordered_data(sys.argv[1])

# Obliczenie prawdopodobieństwa bayesowskiego dla niekompletnych wierszy
# i wyprowadzenie skompletowanych wierszy

completed_data = bayes_probability(
    heading, complete_data, incomplete_data, enquired_column)
print completed_data
