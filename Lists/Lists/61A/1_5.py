
#http://composingprograms.com/pages/15-control.html

from operator import mul
from math import pi

def square(x):
    return mul(x, x) # Watch out! This call doesn't return a value.

x = square(4)
assert x == 15
#        0      1     2      3       4
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):    #range(len(a)) = range(5) -> 0..4
     print(i, a[i])

 #    a[i]  i is index

  #   a[0] a[3]
a = [1, 2, -1, 5, -6]
for x in a[ : ]:      # Loop over a slice copy of the entire list.
    if x == 0: a.remove(x)
print(a)


def print_square(x):
    print(square(x))

print_square(3)

# x = 3, y=5
# 
def percent(x,y):
    dif = abs(x-y)
    return 100 * dif/x

print(percent(3, 5))

def absolutevalue(x):
    if x > 0:
        return x
    elif x == 0:
        return 0
    else: 
        return -x

absolutevalue(-10)
print(absolutevalue(-10))

print(4 < 2)
print(5>3)

'''
Remember that commas seperate multiple names and values in an assignment statement. The line:
pred, curr = curr, pred + curr
has the effect of rebinding the name pred to the value of curr, and 
simultanously rebinding curr to the value of pred + curr. All of the expressions to the right of = 
are evaluated before any rebinding takes place.
'''
#1 0  a
#2 1  b
# a+b
#computer the nth fab
def fib(n):  
   if (n == 1):
       return 0
   if (n == 2):
       return 1
   k=3    
   prev = 0
   next = 1
   while k <= n:
        result = prev + next
        prev = next
        next = result
        k = k+1
   return result


assert (fib(2) == 1)
assert(fib(8) == 13)

x =input()
