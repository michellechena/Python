
#http://www-inst.eecs.berkeley.edu/~selfpace/class/cs9h/
 

print(not '' or not 0 and False )

print(13 and False)

print(1 or 2   )   #1   x or y: x is false, y, x is true x
print(1 or 4  ) #1
print (1 and 2) #2             # x and y: x is false, x, x is true y
print ('' and 3 )   #''

print(not True and 2) 

def bake(cake, make):
     m=1
     if cake == 0:
         cake = cake + 1
         print(cake)
     if cake == 1:
        m=2
     else:
        return cake
     return make

bake(1, "mashed potatoes")

bake(0, 29)



def compose22(f, x, n):
    while n!= 0:
        x = f(x)
        n -= 1
    return x

def square(x):
  return pow(x, 2)

print ('compose22(square, 6, 2)')
print(compose22(square, 6, 2))  # big number 18446744073709551616

def opposite(b):
    return not b
compose22(opposite, 4, True)
compose22(opposite, 5, True)
compose22(opposite, 631, 1)
compose22(opposite, 3, 0)



def double_eights1(n):
    chars = str(n)
    if '88' not in chars:
        return False
    else:
        return True
        


double_eights1(8)  #false

double_eights1(88)  #true

double_eights1(880088)  #true
double_eights1(12345)  #false

double_eights1(80808080) #false

print(4/2)
print(8/2)
print(3//2)
print(3/2)





dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict['Name'] )

d = {'x':1, 'y':2, 'z':3}
d1 = {'x':'a', 'y':'b', 'z':'c'}

print(dict.items())


print(0 or 4 and 2 or 7)
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
        num_of_student +=1

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

            {}
            a = ()

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

'hello string'
['hello', 'string']
def mystery(x):
    a = {}                #{'h':["hello"], "s":["string"]}
    for y in x.split():
        z = y[0]              #a['h'] =['hello']
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
y = x.split(' ')  ['hello','world']
['hello', 'world']
z = list(y[0])  [ 'h','e','l','l','o']
print(z)

print (x.split( ))

print (x.split(' ', 1 ))


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict.items()

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
letters[2:5] =[]
letters="hello"
letters[2:3]='c'


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