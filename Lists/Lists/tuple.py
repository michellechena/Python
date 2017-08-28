#https://www.tutorialspoint.com/python/python_tuples.htm
a = 'hello'
a[0] = 'b'
'''
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
'''

tup1 = ()

tup1=(1,)
tup2 = (1, 2, 3, 4)

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
tup3 = tup1 + tup2;
print (tup3)

#Tuples are immutable which means you cannot update or 
##change the values of tuple elements. 
##You are able to take portions of existing tuples to create new tuples as the following example demonstrates −

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3)



tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
del tup;
print ("After deleting tup : ")
print (tup)

len((1, 2, 3))
(1, 2, 3) + (4, 5, 6)
('Hi!',) * 4
3 in [1, 2, 3]
for x in (1, 2, 3): print (x)

#indexing, slicing, matrixing
      0        1       2
     -3        -2      -1
L = ('spam', 'Spam', 'SPAM!')
L[0]
L[-1]
L[-2]
L[1:]
L[:]
L.reverse()
L[::-1]

x, y = 1, 2
x, y = 1, 2


x , y , z = 1, 3, 5

print ("Value of x , y : ", x,y)

#cmp, min, max, len, tuple(convert a list into tuple)