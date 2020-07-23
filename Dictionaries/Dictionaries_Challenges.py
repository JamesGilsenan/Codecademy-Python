def sum_values(my_dictionary):
  total = 0
  for element in my_dictionary.values():
    total += element
  return total
  
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6