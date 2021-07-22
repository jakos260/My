def extend_list(*arg):
    list_to_return = list()
    for temp_list in arg:
        for item in temp_list:
            if item in list_to_return:
                pass
            else:
                list_to_return.append(item)
    return list_to_return
list_1 = [1, 2, 3, 4, 15]
list_2 = [3, 4, 5, 6]
list_3 = [6, 7, 8]
list_4 = [8, 9, 10]
print(extend_list(list_1, list_2, list_3))
