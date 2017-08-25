
#https://inst.eecs.berkeley.edu/~cs61a/fa16/hw/hw01/

#http://codingbat.com/doc/python-example-code.html

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = a -b 
    else:
        f =  a+b
    return f


print(a_plus_abs_b(1, 2))

#Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. Use only a single line for the body of the function.
def two_of_three(a, b, c):
    return a**2 + b **2 + c ** 2 - min([a,b,c]) **2

print(two_of_three(2,3, 4))


#Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.
def largest_factor(n):
    factors=[]
    for i in range(2,n):
       if (n % i == 0):
        factors.append(i)
    return max(factors)

print(largest_factor(10))

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


nums = [1, 2, 13, 1, 13]
print(sum13(nums))


print(skip13s(nums))