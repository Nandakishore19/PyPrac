from functools import wraps
x = "global x"

def level_one():
    return x

def level_two(v):
    print(v)
    if v:
        x = "local x"
    return x

def level_three():
    
    def inner(y):
        return x,y,z
    z = "outer z"
    return inner('y arg')

def level_four():
    z = "first outer z"
    def inner(y):
        return x,y,z
    z = "second outer z"
    return inner("y arg")
# print(level_four())
#Closure wraps up a functionf


def compose():
    x = 'Nanda'
    def greet(y):
        return "{} {}".format(y,x)
    return greet

# greeting = compose()
# print(greeting("Hello"))
# print(greeting("Bye"))
# print(greeting("Wlcome"))


def func_for_decorate(func):
    def wrapper_func(val):
        return "{}".format(func(val))
    return wrapper_func    

@func_for_decorate
def naming(name):
    return "Nanda {}".format(name)

# temp  = func_for_decorate(naming)
# print(temp("Kishore"))
#naming = func_for_decorate(naming)
# print(naming("Kishore"))


def p_decorate(func):
    @wraps(func)
    def p_wrapper_func(name):
        return "<p>{}</p>".format(func(name))
    return p_wrapper_func
def strong_decorate(func):
    @wraps(func)
    def s_wrapper_func(name):
        return "<strong> {} </strong>".format(func(name))
    return s_wrapper_func

def div_decorate(func):
    @wraps(func)
    def d_wrapper_func(name):
        return "<div> {} </div>".format(func(name))
    return d_wrapper_func

@div_decorate
@strong_decorate
@p_decorate
def get_name(name):
    return "lorem ipsum, {0}".format(name)
# print(get_name.__name__)
# print(get_name("Kishore"))

#Passing arguments to decorators
def tags(tag_name):
    def tag_decorator(func):
        def wrapper_func(name):
            return "<{0}>{1}</{0}>".format(tag_name,func(name))
        return wrapper_func
    return tag_decorator

@tags('p')
def get_text(name):
    return "Hello {}".format(name)

print(get_text("Nanda"))