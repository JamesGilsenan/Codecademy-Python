def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper

def print_my_name():
    print("John")

def print_joes_name():
    print("Joe")

decorated_function = title_decorator(print_my_name)
#decorated_function = title_decorator(print_joes_name)
decorated_function()