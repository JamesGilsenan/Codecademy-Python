def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    expenses = food_bill + electricity_bill + internet_bill + rent
    if budget < expenses:
        return True
    else:
        return False

def twice_as_large(num1, num2):
    if num1 > num2 *2:
        return True
    else:
        return False

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False

print(large_power(10,22))
print(over_budget(500, 100, 40, 60, 350))
print(twice_as_large(6,2))
print(divisible_by_ten(25))
print(not_sum_to_ten(6,6))