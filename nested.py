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
print(level_four())
#Closure wraps up a functionf