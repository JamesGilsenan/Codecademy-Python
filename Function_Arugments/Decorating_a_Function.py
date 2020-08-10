def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper

@title_decorator
def print_my_name():
    print("John")

@title_decorator
def print_joes_name():
    print("Joe")

#decorated_function = title_decorator(print_my_name)
#decorated_function = title_decorator(print_joes_name)
#decorated_function()
print_my_name()