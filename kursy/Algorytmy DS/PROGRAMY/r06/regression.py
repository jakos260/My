#-*- coding: utf_8 -*-

# Uczenie prostego modelu liniowego na podstawie regresji liniowej
import math
import sys
sys.path.append('../common')
import common  # noqa

# Obliczenie gradientu, zgodnie z ktorym bedzie aktualizowany wektor modelu

def linear_gradient(data, old_parameter):
    gradient = [0.0, 0.0]
    for (x, y) in data:
        term = float(y) - old_parameter[0] - old_parameter[1] * float(x)
        gradient[0] += term
        gradient[1] += term * float(x)
    return gradient


# Zastosowanie gradientu do wyliczenia optymalnych skladowych wektora modelu 

def learn_linear_parameter(data, learning_rate,
                           acceptable_error, LIMIT):
    parameter = [1.0, 1.0]
    old_parameter = [1.0, 1.0]
    for i in range(0, LIMIT):
        gradient = linear_gradient(data, old_parameter)
        # aktualizacja parametru zgodnie z regula sredniego bledu kwadratowego
        parameter[0] = old_parameter[0] + learning_rate * gradient[0]
        parameter[1] = old_parameter[1] + learning_rate * gradient[1]
        
        
        # Porownanie postepu iteracji z dopuszczalnym bledem
        # i ewentualne zakonczenie procesu iteracyjnego
        
        if (abs(parameter[0] - old_parameter[0]) <= acceptable_error) and (abs(parameter[1] - old_parameter[1]) <= acceptable_error):
            return parameter
        old_parameter[0] = parameter[0]
        old_parameter[1] = parameter[1]
    return parameter

# Obliczenie wartoosci zmiennej zaleznej na podstawie modelu

def predict_unknown(data, linear_parameter):
    for (x, y) in data:
        print(x, linear_parameter[0] + linear_parameter[1] * float(x))


# Start programu
if len(sys.argv) < 2:
    sys.exit('Prosze podac nazwe pliku wejsciowego. \n')

csv_file_name = sys.argv[1]
# Maksymalna liczba iteracji
LIMIT = 100

# Arbitralne wartosci parametrow procesu
learning_rate = 0.0000001
acceptable_error = 0.001

(heading, complete_data, incomplete_data,
 enquired_column) = common.csv_file_to_ordered_data(csv_file_name)

linear_parameter = learn_linear_parameter(
    complete_data, learning_rate, acceptable_error, LIMIT)
print("Model liniowy:\n(p0,p1)=" + str(linear_parameter) + "\n")

print("Niewiadome na podstawie modelu:")
predict_unknown(incomplete_data, linear_parameter)
