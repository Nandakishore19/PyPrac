import requests
import inspect
r = requests.get("http://httpbin.org/ip")

# print(r.content)
# print(inspect.getmembers(r))
# print(inspect.getsource(requests.Request))
# print(inspect.getdoc(requests.Request))
class A:
    pass
class B(A):
    pass
class C(A):
    pass
tree = inspect.getclasstree([A,B,C])
print(tree)