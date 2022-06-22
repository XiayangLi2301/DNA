from itertools import combinations

def per(temp_list,n):
    temp_list2 = []
    temp_list1 = []
    for c in combinations(temp_list,n):
        temp_list2.append(c)
    for i in temp_list2:
        temp_list1.append(list(i))
    return temp_list1






