#https://docs.python.org/2.3/whatsnew/section-slices.html

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



print(not '' or not 0 and False )

print(13 and False)

print(1 or 2   )   #1   x or y: x is false, y, x is true x
print(1 or 4  ) #1
print (1 and 2) #2             # x and y: x is false, x, x is true y
print ('' and 3 )   #''

print(not True and 2) 


L = range(10)  #0..9
L[::2]
[0, 2, 4, 6, 8]

L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

s='abcd'
s[::2]
'ac'
s[::-1]
'dcba'


a = range(3)
a
[0, 1, 2]
a[1:3] = [4, 5, 6]
a
[0, 4, 5, 6]


#If you have a mutable sequence such as a list or an array#
#you can assign to or delete an extended slice, 
##but there are some differences between assignment to extended and 
#regular slices. Assignment to a regular slice can be used to change the length of the sequence: 
a = range(4)

[0, 1, 2, 3]
a[::2]
[0, 2]
a[::2] = [0, -1]
a
[0, 1, -1, 3]
a[::2] = [0,1,2]  #error

for i in range(3, 6)   #3, 4,5

'''
range([start], stop[, step])
start: Starting number of the sequence.
stop: Generate numbers up to, but not including this number.
step: Difference between each number in the sequence
'''

range(10)[slice(0, 5, 2)]
[0, 2, 4]
