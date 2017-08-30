#and x and y x if x is false,     otherwise y
#0 , '' [] {} false



#x and y: returns x if x is false, y otherwise
print(0 and 4)  #-> 0
print(1 and 4)   #-> 1

#x or y: returns y if x is false, x otherwise

print(0 or 4) #-> 4
print(1 or 4) #-> 1


print([] and 4)
print(2 and 4)

print(3//5)  #floor 
print(3%5)
print(-3%5)
print(5//5)
print(7//5)
print(7/5)
print(2//2)




#x and y: returns x if x is false, y otherwise
0 and 4   #-> 0
1 and 4   #-> 1

#x or y: returns y if x is false, x otherwise

0 or 4 #-> 4
1 or 4 #-> 1


print('22' and 4)
print([1, 2] and 4)

print(0 or 4)  #x is false, return y, x is true, return y


input()

#https://cs61a.org/lab/lab01/
"""Lab 1: Expressions and Control Structures"""

# Coding Practice
'''
Returns the result of composing f n times on x.
'''

'''
def repeated(f, n, x): 
    if n==0:
        return (lambda x: x)
    return (lambda x: f (repeated(f, n-1, x)))
'''
def square(x):
    return x*x


def compose22(f, x, n):
    while n!= 0:
        x = f(x)
        n -= 1
    return x

def square(x):
  return pow(x, 2)

print(compose22(square, 2, 3)) # square(square(3)), or 3 ** 4

print(compose22(square, 1, 4))  # square(4)

print(compose22(square, 6, 2))  # big number 18446744073709551616

def opposite(b):
    return not b
compose22(opposite, 4, True)
compose22(opposite, 5, True)
compose22(opposite, 631, 1)
compose22(opposite, 3, 0)



#composing f n times on x

def compose(f, x, n):
  if n == 0:
    return x
  return compose(f, f(x), n - 1)

def square(x):
  return pow(x, 2)

y = compose(square, 2, 6)
print (y)


def repeated(f, n, x):
  if n == 0:
    return x
  return repeated(f,  n- 1, f(x))

def compose(f, x, n):
  if n == 0:
    return x
  return compose(f, f(x), n - 1)

def square(x):
  return pow(x, 2)

print(repeated(square, 2, 3)) # square(square(3)), or 3 ** 4

print(repeated(square, 1, 4))  # square(4)

print(repeated(square, 6, 2))  # big number 18446744073709551616

def opposite(b):
    return not b
repeated(opposite, 4, True)
repeated(opposite, 5, True)
repeated(opposite, 631, 1)
repeated(opposite, 3, 0)

x = repeated(opposite, 4, True)


'''
    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
'''

"""
Sum all the digits of n.
"""

def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum

sum_digits(10) # 1 + 0 = 1

sum_digits(4224) # 4 + 2 + 2 + 4 = 12
sum_digits(1234567890) # 45

"""
Return true if n has two eights in a row.
"""
#false, true False, True, i+=1, i++, 
def double_eights(n):
    chars = str(n)
    found= False
    i=0
    while i < len(chars)-1:
        if (chars[i] == '8' and chars[i+1] =='8'):
           found = True
        i +=1
    return found
    
def double_eights1(n):
    chars = str(n)
    if (not chars.contains('88')):
        return False
    else:
        return True
        


double_eights1(8)  #false

double_eights1(88)  #true

double_eights1(880088)  #true
double_eights1(12345)  #false

double_eights(80808080) #false
input()
