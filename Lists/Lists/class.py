
https://www.youtube.com/watch?v=jCzT9XFZ5bw&index=6&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
class Critter(object):
    def talk(self):
        print("hi")

crit = Critter()
crit.talk()

import datetime

#https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

# inherit attributes and methods
# subclass, functionality of parent
# override, add new without affecting parent
# classes and instances

x = Employee('cindy','koh', 10000000)
# global variable....???
class Employee: 
    # class varible
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first,middle, last, pay):   #dunder constructor java
        self.first = first
        self.middle = middle
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.net'
        Employee.num_of_emps  +=1
#dunder
    def __repr__(self):  #debugging, logging
        return "Employee('{}','{}','{}')".format(self.first,self.last)

    def __str__(self):   #readable repr ofan object, used to display to the enduser
        return'{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other): #add two employees together emp1.pay + emp2.pay
        return self.pay + other.pay

    
    def __len__(self): #4 characters long
        return len(self.fullname())

    def fullname(self):  #self not there...???
        print(first + ' ' + last)
        return '{} {}'.format(self.first, self.last)   ##

    def apply_raise(self):  #instance variable
        self.pay = int(self.pay * Employee.raise_amount)  #self.raise_amount 


    @property  #getter
    def email(self):  #first, last, email
        return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):  # Cindy Kohl
        first, last = name.split(' ')
        self.first = first
        self.last = last
 

    @fullname.deleter
    def fullname(self):
        print('Delete name:')
        self.first = None
        self.last = None

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

        '''
        Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: classmethod must have a reference to a class object as the first parameter, whereas staticmethod can have no parameters at all.        ;
       an instance method knows its instance (and from that, its class)
a class method knows its class
a static method doesn't know its class or instance
https://softwareengineering.stackexchange.com/questions/306092/what-are-class-methods-and-instance-methods-in-python
       '''
    @classmethod  #as an alternative constructor  ???
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  #receive

    @staticmethod #decorator
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True

class Developer(Employee):  #customize a bit  developer: implement employee
     raise_amt = 1.10

     def __init__(self, first, last, pay, prog_lang):  #dry not repeat the same logic maintainable
         super().__init__(first, last, pay)
      #   Employee.__init__(self, first, last, pay)
         self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super.__init__(first, last, pay)
        if employees is None:
             self.employees = [] #empty list
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# operator overloading, special methods
1+2
'a'+'b'
emp_1 = Employee('Cindy', 'Kohl', 500)
emp_2 = Employee('Weiying','Chen', 100)
emp_1.fullname = 'Cindy Kohl'
del emp_1.fullname
print(emp_1 + emp_2)

#easier to maintain
dev_1 = Developer('First','Last',1000, 'Python')  #look init in dev, walk up the chain of inheritance : method resolution order
dev_2 = Developer('First','Last',1000, 'Python')  #look init in dev, walk up the chain of inheritance : method resolution order

mgr_1 = Manager('Sue','Smith','90000', [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

isInstance(mgr_1, Manager) # object is an instance of class 
isInstance(mgr_1, Employee) #True
isInstance(mgr_1, Developer) #False

isSubclass(Manager, Employee) #True
print(help(Developer))

'''
Employee.set_raise_amt(1.05)
emp_str_1 = 'Cindy-Ko-8888'
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
x = Employee.fullname(new_emp_1)
print(x)

emp_1 = Employee('Cindy','kickasss', 1000000)
emp_2 = Employee('Weiying', 'Chen', 2000000)
emp_str_1 = 'Weiying-Chen-7000'
emp_3 = Employee.from_string(emp_str_1)
print(emp_3.first, emp_3.last)
import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

q, p = 1, 2
print(q, p, p * q, sep=",")
1, 2, 2
'''
#cls
#self
#static: don't pass anything autatically, regular function







        # class methods
        # static methods
 # regular methods: take the instance as the first argument (self)
