add = lambda x,y:x+y
# print(add(2,3))

nums = [1,2,3,4]
nums2 = [2,3,4]
# res = map(lambda x,y:x+y,nums,nums2)
l = ['sat','bat','mat','cat']
res = map(list,l)
# print(*res)

li = [1,2,3,4,5,6,7,8,9,10]

res = tuple(map(lambda x:x**x,li))
# print(res)

class Circle:
    def __init__(self,radius) -> None:
        self._radius = radius
    @property
    def radius(self):
        print("Get Radius")
        return self._radius
    @radius.setter
    def radius(self,rad):
        print("Set radius")
        self._radius = rad
    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius



x = Circle(1)
x.radius = 2
print(x.radius)
del x.radius