#Functions are objects

def get_math_function(operation):
    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2

    if operation == "+":
        return add
    elif operation == "-":
        return subtract


add_function = get_math_function("+")
sub_function = get_math_function("-")
print(sub_function(10, 5))