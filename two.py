add = lambda x,y:x+y
# print(add(2,3))

nums = [1,2,3,4]
nums2 = [2,3,4]
# res = map(lambda x,y:x+y,nums,nums2)
l = ['sat','bat','mat','cat']
res = map(list,l)
# print(*res)

li = [1,2,3,4,5,6,7,8,9,10]

res = (tuple(map(lambda x:x**x,li)))
print(res)