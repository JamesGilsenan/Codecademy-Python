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

def add_ten(my_dictionary):
    for key in my_dictionary:
        my_dictionary[key] += 10
    return my_dictionary

def values_that_are_keys(my_dictionary):
    matches = []
    for key in my_dictionary:
        for value in my_dictionary.values():
            if value == key:
                matches.append(value)
    return matches

def max_key(my_dictionary):
    largest_value = float("-inf")
    largest_key = ""
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key


print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"