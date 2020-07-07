def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

def add_greetings(names):
    greetings = []
    for name in names:
        name = "Hello, " + name
        greetings.append(name)
    return greetings

def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

def odd_indices(lst):
    odd_index_lst = []
    for i in range(len(lst)):
        if i % 2 == 1:
            odd_index_lst.append(lst[i])
    return odd_index_lst


print(divisible_by_ten([20, 25, 30, 35, 40]))
print(add_greetings(["Tom", "Dick", "Harry"]))
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(odd_indices([4, 3, 7, 10, 11, -2]))