def sum_naturals(n):
    total, k=0,1
    while k <= n:
        total, k = total+k, k+1
    return total


assert (sum_naturals(5) == 15)

''' 
high order function
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
'''

print (18 / 4)

#https://www.tutorialspoint.com/python/python_strings.htm

#https://www.youtube.com/watch?v=UhziRgmVKuQ

# {} an empty dictionary
# [] an empty list

{'h': ['hello', 'hi'],
'w': ['world']}

def mystery(x):
    a = {}
    for y in x.split():
        z = y[0]              #a['h'] =['hello','hi']
        if z not in a:
            a[z] = []           
        a[z].append(y)        
    return a

x = 'hello world  hi  test'


y='hello'
y[0] y[3] y[5]
[hello,
world, 
hi, 
test]

print(mystery(x))
mystery(x)
input()




#http://docs.python.org/library/collections.html#collections.namedtuple 
from collections import namedtuple


mytype = namedtuple("mytype", "foo bar baz")

a = mytype(1,2,3)
a.foo
1
a.bar
2
a.baz
 3