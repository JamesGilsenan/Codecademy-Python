def is_leap(year):
    #all statements evalueate to booleans, therefore function returns a boolean
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

def print_ints(n):
    nums = ""
    for i in range(1, n+1):
        nums += str(i)
    return nums

print(is_leap(2100))
print(print_ints(5))