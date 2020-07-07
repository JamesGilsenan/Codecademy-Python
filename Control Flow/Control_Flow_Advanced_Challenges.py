def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False

def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False    

def always_false(num):
    if num > num or num < num:
        return True
    else:
        return False

def movie_review(rating):
    if rating >= 9:
        return "Outstanding!"
    elif rating >=5:
        return "This one was fun."
    else:
        return "Avoid at all costs!"

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"

print(in_range(10, 1, 20))
print(same_name("Jim", "Jim"))
print(always_false(5))
print(movie_review(9))
print(max_num(1,2,2))