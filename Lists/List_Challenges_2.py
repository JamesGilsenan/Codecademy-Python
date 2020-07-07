def every_three_nums(start):
    return list(range(start, 101, 3))
    
def remove_middle(lst, start, end):
    sublst1 = lst[:start]
    sublst2 = lst[end+1:]
    new_lst = sublst1 + sublst2
    return new_lst

def more_frequent_item(lst, item1, item2):
    count_item1 = lst.count(item1)
    count_item2 = lst.count(item2)
    if count_item1 > count_item2:
        return item1
    elif count_item2 > count_item1:
        return item2
    else:
        return item1

def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        lst[index] = lst[index] * 2
        return lst

def middle_element(lst):
    if len(lst) % 2 == 0:
        middle1 = (len(lst) / 2) - 1
        middle2 = (len(lst) / 2)
        m1 = lst[int(middle1)]
        m2 = lst[int(middle2)]
        return (m1 + m2) / 2
    else:
        middle = len(lst) / 2
        return lst[int(middle)]

print(every_three_nums(91))
print(remove_middle([1,2,3,4,5,6,7,8,9], 2, 6))
print(more_frequent_item([1,2,2,3,4,5,5,5,6,7,7,7,7,8], 2,7))
print(double_index([1,2,3,4,5], 3))
print(middle_element([1,2,3,4,5,6]))