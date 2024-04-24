import time

# start = datetime.now()

# a = 0
# for i in range(1000):
#     a+=(i*100)

# end = datetime.now()

# td = (end-start).total_seconds()*10**3

# print(f'the time for execution is {td:.3f}ms')

def decorator_func(func):
    def wrapper_func():
        start = time.time()
        res = func()
        end = time.time()
        td = (end-start)*10**3
        print(f'Function {func.__name__} executed in time {td:.3f}ms')
        return res
    return wrapper_func

# @decorator_func
def func():
    # print("This functions execution time is tested.")
    time.sleep(1)
    

@decorator_func
def func2():
    # print("function 2 is executing and its time will be printed")
    time.sleep(2)
    
test = decorator_func(func)
test()
# func()
func2()