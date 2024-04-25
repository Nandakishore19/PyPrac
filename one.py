import random
from collections import namedtuple
# print("Hello")
# name = input("Enter your name:")
# print(f"Hello {name}, welcome back")
# m, n = map(int, input().split())
# print(m ,n)
# str, *lst = input().split()
# print(str,lst)
# n = random.randrange(1,7)
# print(n)
# print("One") if (1==1) else print("Two")
# x = float(4)
# print(x)

# def my_function(n):
#     print(f"Function {n}")
#     return "nanda"

# x = my_function("ff")

# def arbitary(*args):
#     print(args)

# arbitary("Nanda",1,"Kishore")
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# list = [1,1,1,1]
# print(list)
# def test(**names):
#    x = names["one"]
#    y = names["two"]
#    print("I dont know mate" + x+ y)

# test(one = "Nanda", two = "Kishore", three = "Gorenka")
# print("We are the so-called \"Vikings\" of the north")
# txt = "Hello\rNanda"
# print(txt)
# def func(name = "Nanda"):
#     print(f"My name is {name}")

# func()
# func("nanda")
# func("kishore")


lis = [1,2,3,4,5,6,7,8,9]
lis2 = [23,56]
# print(lis+lis2)
# x= list((1,2,3))
# print(x)
# print(lis[6:])
# lis.insert(2,10)
# print(lis)
# lis.sort()
# lis.append(11)
# lis.extend(lis2)
# print(lis)
# print(lis.count(1))
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
# print(x[0][0])

# print(*x[0])

# a,b = 0,1
# i=0
# while i<10:
#     print(a,end="\t")
#     i = i+1
#     a,b = b,a+b


tup = (1,2,3,"nanda")
for x in tup:
    # print(x)
    pass

single = ("nanda")
# print(len(single))
# print(single)

def increment(number):
    def inner_increment():
        return number+1
    return inner_increment()


# print(increment(11))

# def outer():
#     def _inner():
#         print("This is global")


 
def logger(msg):
    def log_message():
        print('Log: ',msg)
    return log_message
# log_hi = logger('Hi!')
# log_hi()
# log_hi()
# log_hi()

# import sys
# import gc
# x = [1,2,3]
# y = x
# y= None
# gc.enable()
# del x
# # ref_count = sys.getrefcount(x)
# # print(ref_count)
# print(gc.collect())

# op = open('task.txt')
# print(dir(op))
x = 5
# print(id(x))
# print(getattr(logger,'msg','default'))

class Test:
    pass
class Child(Test):
    pass

x = Child()
print(isinstance(x,Test))
# print(dir(__builtins__))
# print(vars(Test))
# print(setattr(Test,'name','Nanda'))
print(x.__dict__)

t = namedtuple('Car','Color make year')
my_car = t('white','Wagonr','2020')
print(my_car.Color)