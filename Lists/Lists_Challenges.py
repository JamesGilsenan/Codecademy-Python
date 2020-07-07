def append_sum(lst):
    second_last = len(lst) - 2
    result = lst[second_last] + lst[-1]
    lst.append(result)
    second_last = len(lst) - 2
    result = lst[second_last] + lst[-1]
    lst.append(result)
    second_last = len(lst) - 2
    result = lst[second_last] + lst[-1]
    lst.append(result)
    return lst

def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    elif len(lst2) > len(lst1):
        return lst2[-1]
    else:
        return lst1[-1]

def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False

def append_size(lst):
    lst.append(len(lst))
    return lst

def combine_sort(lst1, lst2):
    lst1 = lst1 + lst2
    lst1.sort()
    return lst1

print(list(append_sum([1,1,2])))
print(larger_list([1,2,3], [1,2,3,4]))
print(more_than_n([1,2,3,4,5,3,6,3], 3, 2))
print(append_size([10,20,30]))
print(combine_sort([1,3,2], [6,5,4,7,8]))