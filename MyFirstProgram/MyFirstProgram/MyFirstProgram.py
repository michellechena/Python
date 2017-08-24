#https://docs.python.org/3/tutorial/introduction.html#lists

# Fibonacci series
# the sum of two numbers defines the next

#multiple assignment
# anything with non-zero length (value) is true
# only zero false, empty sequence false

a, b = 0, 1

while (b<1000): 
    print(b, end=',')
    a, b = b, a+b


a, b = 0, 1
while(b<10) : 
    print(b)
    a, b = b, a+b


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

'''
If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:
'''
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)

# this will create an infinite list
#for w in words:  
#    if len(w) > 6:
#        words.insert(0, w)
#print(words)  # bug!!!

#If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
for i in range(5):
    print(i)


'''
The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):
'''

range(5, 10)   # 5 through 9
range(0, 10, 3) # 0, 3, 6, 9
range(-10, -100, -30)  # -10, -40, -70


#To iterate over the indices of a sequence, 

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print (i, a[i])

'''
In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.
We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the for statement is such an iterator. The function list() is another; it creates lists from iterables:
'''
print(range(10))

print(list(range(5)))


#The break statement, like in C, breaks out of the innermost enclosing for or while loop.
'''
Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. This is exemplified by the following loop, which searches for prime numbers:
'''
for n in range(2, 10):
    for x in range(2, n):
            if  n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
    else:
          #loop fell through without finding a factor
          print(n, 'is a prime number')


x = int(input("Please enter an integer:"))
if x < 0: 
    x = 0
    print("negative changed to zero")
elif x == 0: 
    print('zero')

elif x == 1:
    print('single')
else: 
     print('more')



# The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range (2, 10): 
    if num % 2 == 0: 
        print("found an even number", num)
        continue
    print("found a number", num)


#pass statement does nothing
#while True: 
#    pass

#class MyEmptyClass:
#     pass

#def initLog(*args):
#     pass


a = [1, 2, -1, 5, -6]
for x in a[ : ]:      # Loop over a slice copy of the entire list.
    if x < 0: a.remove(x)
print(a)