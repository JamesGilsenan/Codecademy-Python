def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return num *3

def tip(total, percentage):
    result = total * (percentage / 100)
    return result

def introduction(first_name, last_name):
    return last_name+ ", " + first_name + " " + last_name

def dog_years(name, age):
    dog_age = age * 7
    return name + ", you are " + str(dog_age) + " years old in dog years"

def lots_of_math(a,b,c,d):
    result_one = a + b
    print(result_one)
    result_two = c-d
    print(result_two)
    result_three = result_one * result_two
    print(result_three)
    return result_three % a


first_three_multiples(10)
print(tip(100, 15))
print(introduction("James", "Bond"))
print(dog_years("Rio", 15))
print(lots_of_math(1,2,3,4))
