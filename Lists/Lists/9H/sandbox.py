class Critter(object):
    def talk(self):
        print("hi")

crit = Critter()
crit.talk()

class Student():
    num_of_student = 0   #class variable

    def __init__(self, first, last):
        self.first = first    # first: instance variable
        self.last = last      # last: instance variable

    def learn(self):  #instance method => self
        print("learn myself instance")

    @classmethod
    def learnc(cls):  #class method => >cls
        print("learn myself class")

    @staticmethod
    def staticmethod():
        return 'static method called'

class HonorStudent(Student):  #honor student is a student, it inherits from student
    def __init__(self, first, last, awards):
        super.__init__(first, last)

        if awards is None:
             self.awards = [] #empty list
        else:
            self.awards = awards

honorStudent = HonorStudent('First','LastName', ['A', 'A'])   

student1 = Student()
student1.learn()

Student.learnc()
x = Student.staticmethod()
print(x)




from operator import mul

def square(x):
    return mul(x, x) # Watch out! This call doesn't return a value.

x = square(4)
assert x == 15

#AssertError

def mystery(x):
    a = {}
    for y in x.split():
        z = y[0]              #a['h'] =['hello','hi']
        if z not in a:
            a[z] = []           
        a[z].append(y)        
 
    return a

x = 'hello world  hi  test'

print(mystery(x))

'''
The method split() returns a list of all the words in the string, 
using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
'''
x = 'hello world'
y = x.split(' ')
['hello', 'world']
z = list(y[0])
print(z)

print (x.split( ))

print (x.split(' ', 1 ))


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


def rev(nums):
    return nums.reverse()

a = [1,3,5]  #[5,3,1]
rev(a)
print(a)


L = ('spam', 'Spam', 'SPAM!')
a = [1,2, 4]
a.reverse()

c=[33,34]
print(list(reversed(c)))

b=[1,3]
print(b[::-1])
print(L[::-1])



print(3 in [1, 2, 3])

print(('Hi!', 'hey') * 4)

nme ='tes'
nme + '3'  #tes3 #error

name="hello"
name[1] ='d'
##??

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = []



def f(x,y):
    return (x+y)**2

f(3, 1)
g = lambda x, y: (x+y)**2

print(g(3, 1))

food = {'egg': 'yes', 'ham': 'yes', 'spam': 'yes'}

print(food.items())
print(food.keys())
print(food.values())  ['egg', 'ham']

#[(egg, yes), (ham, yes), (spam, yes)] 


a = '100, 20, 200'
b = a.split(' ')
print(b)  # a list


print('spam' + str(3) + 'lovely spam')

x = 'hello' #string 
print(len(x))