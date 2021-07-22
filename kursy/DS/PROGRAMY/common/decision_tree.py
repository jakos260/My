#-*- coding: utf_8 -*-

# *** Biblioteka dla drzew decyzyjnych ***
# wykorzystywana na potrzeby konstruowania drzew decyzyjnych
# i lasów losowych

import math
import random
import common
from anytree import Node, RenderTree
from common import printfv, cvstd

# Węzeł drzewa decyzyjnego

class TreeNode:

    def __init__(self, var=None, val=None):
        self.children = []
        self.var = var
        self.val = val

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_var(self):
        return self.var

    def get_val(self):
        return self.val

    def is_root(self):
        return self.var is None and self.val is None

    def is_leaf(self):
        return len(self.children) == 0

    def name(self):
        if self.is_root():
            return "[korzeń]"
        return "[" + self.var + "=" + self.val + "]"

# Classifies the feature to the class decided by the decision tree.


def classify_by_tree(tree, heading, enquired_column, feature):
    var_to_index = {}
    for index in range(0, len(heading)):
        var_to_index[heading[index]] = index
    return classify_by_tree_main(tree, var_to_index, feature)


def classify_by_tree_main(tree, var_to_index, feature):
    if tree.is_leaf():
        return tree.get_val()
    else:
        for child in tree.get_children():
            if child.is_leaf():
                return child.get_val()
            if child.get_val() == feature[
               var_to_index.get(child.get_var())]:
                return classify_by_tree_main(
                       child, var_to_index, feature)
        return None


# Konstruowanie drzewa decyzyjnego.
# "heading" to nagłowek, czyli nazwy atrybutów
# "complete_data" to elementy danych ze znanymi wartościami kazdego atrybutu
# "enquired_column" to indeks kolumny (licząc od zera) zawierającej atrybut decyzyjny. 


def construct_decision_tree(verbose, heading, complete_data, enquired_column):
    return construct_general_tree(verbose, heading, complete_data,
                                  enquired_column, len(heading))


# m jest numerem zmiennej klasyfikującej najbardziej znaczącej dla danego węzła.
# ma znaczenie tylko dla lasów losowych.


def construct_general_tree(verbose, heading, complete_data,
                           enquired_column, m):
    available_columns = []
    for col in range(0, len(heading)):
        if col != enquired_column:
            available_columns.append(col)
    tree = TreeNode()
    printfv(2, verbose, "Rozpoczynamy budowę od korzenia " + 
                        "jako pierwszego węzła w drzewie.\n")
    add_children_to_node(verbose, tree, heading, complete_data,
                         available_columns, enquired_column, m)
    return tree

# Podział zbioru danych na grupy, z których każda wyznaczona jest 
# przez określoną wartość atrybutu w kolumnie "col".

def split_data_by_col(data, col):
    data_groups = {}
    for data_item in data:
        if data_groups.get(data_item[col]) is None:
            data_groups[data_item[col]] = []
        data_groups[data_item[col]].append(data_item)
    return data_groups

# dodanie liścia do węzła macierzystego.


def add_leaf(verbose, node, heading, complete_data, enquired_column):
    leaf_node = TreeNode(heading[enquired_column],
                         complete_data[0][enquired_column])
    printfv(2, verbose,
            "Dodajemy liść " + leaf_node.name() + ".\n")
    node.add_child(leaf_node)

# dodanie do węzła wszystkich jego potomków


def add_children_to_node(verbose, node, heading, complete_data,
                         available_columns, enquired_column, m):
    if len(available_columns) == 0:
                
        printfv(2, verbose, "Nie dysponujemy żadnym atrybutem, na podstawie " +
                "którego moglibyśmy dokonać podziału, " +
                "dodajemy zatem liść do bieżącej gałęzi. ")

        add_leaf(verbose, node, heading, complete_data, enquired_column)
        return -1

    printfv(2, verbose, "Dodajemy węzły potomne do węzła " +
            node.name() + ".\n")

    selected_col = select_col(
        verbose, heading, complete_data, available_columns,
        enquired_column, m)
    for i in range(0, len(available_columns)):
        if available_columns[i] == selected_col:
            available_columns.pop(i)
            break

    data_groups = split_data_by_col(complete_data, selected_col)
    if (len(data_groups.items()) == 1):
        printfv(2, verbose, "Dla wybranej zmiennej " +
                heading[selected_col] +
                " wszystkie dostępne atrybuty mają tę samą wartość " +
                complete_data[0][selected_col] + ". " +
                "Dołączamy więc liść do gałęzi. ")
        add_leaf(verbose, node, heading, complete_data, enquired_column)
        return -1

    if verbose >= 2:
        printfv(2, verbose, "Wykorzystując zmienną " +
                heading[selected_col] +
                " partycjonujemy dane w bieżącym węźle, " +
                " gdzie każda partycja s\danych stanowi jedną z nowych gałęzi " +
                "wychodzących z bieżącego węzła " + node.name() +
                ". " + "utworzono następujące partycje:\n")
        for child_group, child_data in data_groups.items():
            printfv(2, verbose, "Partycja dla " +
                    str(heading[selected_col]) + "=" +
                    str(child_data[0][selected_col]) + ": " +
                    str(child_data) + "\n")
        printfv(
            2, verbose, "Teraz. mając partycje, tworzymy gałęzie " +
                        "i węzły potomne.\n")
    for child_group, child_data in data_groups.items():
        child = TreeNode(heading[selected_col], child_group)
        printfv(2, verbose, "\nDodajemy węzeł potomny " + child.name() +
                " do węzła " + node.name() + ". " +
                "Ta gałąź klasyfikuje %d atrybut(ów): " +
                str(child_data) + "\n", len(child_data))
        add_children_to_node(verbose, child, heading, child_data, list(
            available_columns), enquired_column, m)
        node.add_child(child)
    printfv(2, verbose,
            "\nDodaliśmy wszystkie węzły potomne do węzła " +
            node.name() + ".\n")


# Wybór, spośród dostepnych atrybutów, atrybutu dajacego największy zysk informacyjny


def select_col(verbose, heading, complete_data, available_columns,
               enquired_column, m):
    # Uwzględnienie tylko podzbioru dostępnych kolumn o rozmiarze m
    printfv(2, verbose,
            "Zmienne, które obecnie sa dostępne, to " +
            str(numbers_to_strings(available_columns, heading)) + ". ")
    if len(available_columns) < m:
        printfv(
            2, verbose, "Ponieważ jest ich mniej niż wszkazuje "+
                        "parametr m=%d, uwzględniamy je wszystkie. ", m)
        sample_columns = available_columns
    else:
        sample_columns = random.sample(available_columns, m)
        printfv(2, verbose,
                "Wybieramy ich podzbiór o liczebnści m " +
                str(numbers_to_strings(available_columns, heading)) +
                ".")

    selected_col = -1
    selected_col_information_gain = -1
    for col in sample_columns:
        current_information_gain = col_information_gain(
            complete_data, col, enquired_column)
        # print len(complete_data),col,current_information_gain
        if current_information_gain > selected_col_information_gain:
            selected_col = col
            selected_col_information_gain = current_information_gain
    printfv(2, verbose,
            "Wśród dostepnych zmiennych największy zysk informacyjny daje zmienna " +
            heading[selected_col] +
            ". Wykorzystujemy ją więc jako kryterium podziału." +
            "Jednocześnie usuwamy ją z listy dostępnych zmiennych dla potomków bieżącego węzła. ")
    return selected_col


# Konwersja liczb z listy do postaci znakowej


def numbers_to_strings(numbers, strings):
    string_list = []
    for n in numbers:
        string_list.append(strings[n])
    return string_list


# Obliczanie zysku informacyjnego podczas partycjonowania "complete_data"
# zgodnie z atrybutem w kolumnie "col" i klasyfikacją wg atrybutu z kolumny
# "enquired_column".


def col_information_gain(complete_data, col, enquired_column):
    data_groups = split_data_by_col(complete_data, col)
    information_gain = entropy(complete_data, enquired_column)
    for _, data_group in data_groups.items():
        information_gain -= (float(len(data_group)) / len(complete_data)
                             ) * entropy(data_group, enquired_column)
    return information_gain


# Obliczenie entropii danych klasyfikowanych na popdstawie atrybutu
# w kolumnie "enquired_column".


def entropy(data, enquired_column):
    value_counts = {}
    for data_item in data:
        if value_counts.get(data_item[enquired_column]) is None:
            value_counts[data_item[enquired_column]] = 0
        value_counts[data_item[enquired_column]] += 1
    entropy = 0
    for _, count in value_counts.items():
        probability = float(count) / len(data)
        entropy -= probability * math.log(probability, 2)
    return entropy

# A visual output of a tree using the text characters.


def display_tree(tree):
    anytree = convert_tree_to_anytree(tree)
    for pre, fill, node in RenderTree(anytree):
        
        pre = pre.encode(encoding='UTF-8', errors='strict')
        
        #print ' ***** pre', pre
        # A.Grazynski
        print("%s%s" % (pre, node.name))
        #print("%s%s" % (cvstd(pre), cvstd(node.name)))
        #print "%s%s" % (cvstd(pre), cvstd(node.name))

# A simple textual output of a tree without the visualization.
def display_tree_simple(tree):
    print('***Struktura drzewa***')
    display_node(tree)
    sys.stdout.flush()

# A simple textual output of a node in a tree.


def display_node(node):
    if node.is_leaf():
        print('The node ' + node.name() + ' is a leaf node.')
        return
    sys.stdout.write('The node ' + node.name() + ' has children: ')
    for child in node.get_children():
        sys.stdout.write(child.name() + ' ')
    print('')
    for child in node.get_children():
        display_node(child)

# Convert a decision tree into the anytree module tree format to make
# it ready for rendering.


def convert_tree_to_anytree(tree):
    anytree = Node("Korzeń")      
    attach_children(tree, anytree)
    return anytree

# Attach the children from the decision tree into the anytree
# tree format.


def attach_children(parent_node, parent_anytree_node):
    for child_node in parent_node.get_children():
        child_anytree_node = Node(
            child_node.name(), parent=parent_anytree_node)
        attach_children(child_node, child_anytree_node)
