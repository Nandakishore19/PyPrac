import datetime
class Employee:
    num_ofEmps = 0
    raise_amount = 1.04
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+'.'+lname+'@company.com'
        self.num_ofEmps+=1
    def display_fullname(self):
        print("{}{}".format(self.fname,self.lname))
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_string):
        first,last,pay = emp_string.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
                return False
        return True
# print(Employee.num_ofEmps)
emp1 = Employee("Nanda","Kishore",100)
emp2 = Employee("Kishore","Nanda",200)

my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))
# print(Employee.num_ofEmps)
# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# new_emp = Employee.from_string("Nanda-Kishore-1999")
# print(new_emp.email)
# print(emp1.email)
# emp1.display_fullname()
# emp2.display_fullname()
# Employee.display_fullname(emp1)
# Employee.raise_amount=2
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# print(emp1.__dict__)
 