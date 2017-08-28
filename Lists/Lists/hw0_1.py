

#https://inst.eecs.berkeley.edu/~cs61a/fa16/hw/hw01/

#http://codingbat.com/doc/python-example-code.html



from operator import add, sub

def a_plus_abs_b(a, b):
    if b < 0:
        f = a -b 
    else:
        f = a+b
    return f


c = a_plus_abs_b(1, 2)

#Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. Use only a single line for the body of the function.
def two_of_three(a, b, c):
    return a**2 + b **2 + c ** 2 - min([a,b,c]) **2


print(two_of_three(2,3, 4))


#Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.
def largest_factor(n):
    factors=[]  #[]
    for i in range(2,n):
       if (n % i == 0):
        factors.append(i)
    return max(factors)

print(largest_factor(10))



#
#Arrays can also only data of one type, whereas a list can have entries of various object types.
#Arrays are also more efficient for some numerical computation.
def skip13s(l):
    i = 0
    s = 0
    while (i < len(l)):
        if l[i] == 13:
            i += 1
        else:
            s += l[i]
        i += 1
    return s

#nums = [1, 2, 13, 1, 13]
#print(sum13(nums))


#print(skip13s(nums))
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return c()

def t():
    return t()

def f():
    return f()


print(if_function(True, 2, 3))

print(if_function(False, 2, 3))

print(if_function(3==2, 3+2, 3-2))

print(if_function(3>2, 3+2, 3-2))


