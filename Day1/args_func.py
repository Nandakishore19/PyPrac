def func(tot,char='+',*nums):
    for x in nums:
        if(char == '+'):
            tot+=x
        else:
            tot-=x
    return tot
i = func(100,10,20,30)
print(i)