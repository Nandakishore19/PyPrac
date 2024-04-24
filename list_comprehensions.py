values = []
# for x in range(10):
    # values.append(x)



# values = [x for x in range(10)]
# print(values)
# print(11)
# evens = []
# evens = [x for x in range(50) if x%2==0]
# print(evens)

# options = ["Nanda","Naaanda","nanda","naanda"]
# valid = [x for x in options if len(x)>=2  if x[0]=='N' if x[-1] == 'a']
# print(valid)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# flattened = [num for row in matrix for num in row]
# print(flattened)

# categories = []
# categories = ["even" if x%2==0 else "odd" for x in range(10)]
# print(categories)

lst = []
# for a in range(5):
    # l1= []
    # for b in range(5):
        # l2 = []
    #     for c in range(5):
    #         l2.append(c)
    #     l1.append(l2)
    # lst.append(l1)

# print(lst)
# lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
# print(lst)
def square(x):
    return x**2


squared = [square(x) for x in range(10)]
# print(squared)

list1 = [(x,y) for x in [1,2,3] for y in [3,2,4] if x!= y]
# print(list1)
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Transposed matrix

transposed =[]
# for i in range(len(matrix[0])):
#     listk = []
#     for row in matrix:
#        listk.append(row[i])
#     transposed.append(listk)
   


transposed = [[row[i] for row in matrix]for i in range(len(matrix[0]))]
print(transposed)