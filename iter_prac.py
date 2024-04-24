# nums = [1,2,3]
# i_nums = iter(nums)
# print(i_nums)
# print(next(i_nums))
# # print(next(i_nums))
class MyRange:
    def __init__(self,start,end) -> None:
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current = self.value
        self.value+=1
        return current
    
def my_range(start,end):
    current = start
    while current< end:
        yield current
        current+=1
# nums = MyRange(1,10)
# for num in  nums:
#     print(num)

nums = my_range(1,10)
print(next(nums))
print(next(nums))
