def tenth_power(num):
    result = num ** 10
    return result

def square_root(num):
    result = num ** (1/2)
    return result

def win_percentage(wins, losses):
    percentage_won = (wins / (wins + losses)) * 100
    return percentage_won

def average(num1, num2):
    result = (num1 + num2) / 2
    return result

print(tenth_power(2))
print(square_root(36))
print(win_percentage(5,5))
print(average(4,6))