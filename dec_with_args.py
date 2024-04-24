def prefix_decorator(prefix):
    def decorator_func(og_function):
        def wrapper_func(*args):
            print(prefix,'Executed before', og_function.__name__)
            result = og_function(*args)
            print(prefix, 'Executed After',og_function.__name__)
            return result
        return wrapper_func
    return decorator_func

@prefix_decorator('RESULT:')
def display_info(name,age):
    print('Display info ran with arguments ({}{})'.format(name,age))


display_info('Nanda',21)
display_info('Kishore',22)
