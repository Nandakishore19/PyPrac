from functools import wraps
# def outer(msg):
#     def inner():
#         print(msg)
#     return inner


# my_func = outer('Hi')
# bye_func = outer('Bye')

# my_func()
# bye_func()

def decorator_func(original_function):
    def wrapper_func(*args,**kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_func
@decorator_func
def display():
    print('Display function ran')

# decorated_display = decorator_func(display)

# decorated_display()

# display() TThis is same as the above two lines by creating a decorator we want 
#that
@decorator_func
def display_info(name,age):
    print('Display_info ran with arguments ({} {})'.format(name,age))

display_info('Nanda',21)