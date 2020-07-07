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

def exponents(bases, powers):
    results = []
    for i in range(len(bases)):
        for j in range(len(powers)):
            results.append(bases[i] ** powers[j])
    return results

def larger_sum(lst1, lst2):
    total1 = 0
    total2 = 0
    for i in range(len(lst1)):
        total1 += lst1[i]
    for j in range(len(lst2)):
        total2 += lst2[j]
    if total2 > total1:
        return lst2
    else:
        return lst1

def over_nine_thousand(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
        if total > 9000:
          break
    return total

def max_num(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max

print(divisible_by_ten([20, 25, 30, 35, 40]))
print(add_greetings(["Tom", "Dick", "Harry"]))
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(odd_indices([4, 3, 7, 10, 11, -2]))
print(exponents([2, 3, 4], [1, 2, 3]))
print(larger_sum([1, 9, 5], [2, 3, 7]))
print(over_nine_thousand([8000, 900, 120, 5000]))
print(max_num([50, -10, 0, 75, 20]))