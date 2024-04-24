student = {'name':'nanda Kishore','age':21,'Clg':"NGIT"}
student['phone'] = 12345
student.update({'name':'nanda','phone':123})
del student['age']
# print(student)
print(type(student.keys()))
print(student.items())
for key,val in student.items():
    print(key,val)




# myFamily = {
#     "child1":{
#         "name" : "nanda",
#         "age" : 21
#     },
#     "child2" : {
#         "name" : "kishore",
#         "age" : 22
#     }
# }

child1 = {"name" :"Nanda","age" :21}
child2 = {"name":"Kishore","age":22}
child1.update(child2)
myFamily = {"child1" :child1,"child2":child2}
# print(child1)

Students = {}
id=1
id = {"name":"nanda","age":21,"grade":99}
Students.update(id)
print(Students)
