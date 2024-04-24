def main_admit():
    max_capacity = 10
    curr_capacity=0
    def admit_student():
        nonlocal curr_capacity
        if(curr_capacity<max_capacity):
            curr_capacity+=1
            return "Success!! Student has been admitted"
        else:
            return "Maximum capacity reached"
    return admit_student

admin = main_admit()
print(admin())
print(admin())
print(admin())
print(admin())
print(admin())
print(admin())
print(admin())
print(admin())
print(admin())
print(admin())
print(admin()) 