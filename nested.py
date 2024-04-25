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
print(naming("Kishore"))