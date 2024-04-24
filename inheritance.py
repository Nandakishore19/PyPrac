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

class Developer(Employee):
    raise_amount=1.6
    def __init__(self, fname, lname, pay,prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amount = 2
    def __init__(self, fname, lname, pay,employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def printEmps(self):
        for emp in self.employees:
            print('-->',emp.display_fullname())
dev_1 = Developer('Nanda','Kishore',123,'Python')
dev_2 = Developer('Kishore', 'Gorenka',234,'Java')

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# # print(help(Developer))
# print(dev_1.email)
# print(dev_1.prog_lang)
# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)
# print(dev_2.prog_lang)
# mgr_1 = Manager('Nk','Kish',2345,[dev_1,dev_2])
# print(mgr_1.email)
# print(mgr_1.printEmps())