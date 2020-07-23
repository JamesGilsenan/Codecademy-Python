def sum_values(my_dictionary):
  total = 0
  for element in my_dictionary.values():
    total += element
  return total

def sum_even_keys(my_dictionary):
    total = 0
    for element in my_dictionary:
        if element % 2 == 0:
            total += my_dictionary[element]
    return total

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6