import csv

dict_list = []

filepath = 'D:\Dysk Google\BIOMED\ADP\iris.csv'
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for line in csvreader:
        print(line)
        dict_list.append(line)