students = {}
def gen_key():
    return len(students)+1

def add_student(name,age,grade):
    """"
    Adds a Student to the dict

    name (str):Name of the student
    age(int): Age of the student
    grade(int):Grade of the Student 
    """
    id = gen_key()
    students[id] = {
        "Name":name,
        "Age" : age,
        "Grade": grade
    }
def update_stud(id,new_info):
    students[id].update(new_info)
def remove_student(id):
    del students[id]

def student_details(id):
    return students.get(id, "Student id is invalid")

def get_students_by_grade(grade):
    """
    Returns all the students of a grade

    grade (int) : Required Grade

    list: Students of the given grade
    """
    lst = [id for id,det in students.items() if det['Grade']==grade]
    return lst
def get_all_students():
    sets = {id for id in students.keys()}
    return sets

# add_student("nanda",21,11)
# add_student("kishore",22,22)
# update_stud(2,{"Name":"nan","Age":22})
# remove_student(2)
# print(student_details(3))
# lst = get_students_by_grade(11)
# print(lst)
# print(students)
# print(get_all_students())
print(add_student.__doc__)
while(True):
    inp = int(input("Enter your choice\n 1: Add Student \n 2: Update Student Details\n 3: Remove Student \n 4: Get a student Details\n 5: Get Details of Students in a grade\n 6: List of Students 7: Exit:\n"))
    if(inp==7):
        break
    elif inp==1:
        name = input("Enter students name:")
        age = int(input("Enter students age:"))
        grade = int(input("Enter the grade of the student:"))
        add_student(name,age,grade)
    elif inp==2:
        id = int(input("What is the students id:"))
        #Yet to do
    elif inp ==3:
        id = int(input("Enter the ID of the student you want to remove:"))
        remove_student(id)
    elif inp ==4:
        id = int(input("Enter the id of the student"))
        print(student_details(id))
    elif inp==5:
        grade = int(input("Which Grade?:"))
        print(get_students_by_grade(grade))
    elif inp==6:
        print(get_all_students())
    else:
        print("Not valid Try again")