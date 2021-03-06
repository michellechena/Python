#https://docs.python.org/3/tutorial/introduction.html#lists

#list of comma-separated values (items) between square brackets. Lists might contain items of different types, 
##but usually the items all have the same type.



a = '100, 20, 200'
b = a.split(' ')
print(b)  # a list



'''
[] an empty list [1, 2,4, 5]   ['hello','world', 1, 2, 3.25]
{}  a empty dictionary  key value pair
{ 'key1': 'value1', 'key2':'value2'}
'''




a= [1, 2, 'car',10, 20]
a[2]
a[2][0:2]  #end-1
a[2:]
a[:] 
len(a)

range(0,5)  #the end-1
for x in range(0,len(a)):
   print(a[x])

  
a= [1, 2, '88',10, 20]
for x in a[:]:
    if(int(x)< 5):
       a.remove(x)
print(a)

for x in a:
    if(int(x) < 5):
       a.remove(x)
print(a)

squares = [1, 4, 9, 16, 25]

print(squares)

#lists can be indexed and sliced.
#All slice operations return a new list containing the requested elements

print(squares[-3:-4])


print(squares[::-1])

#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

squares[-3] = 100
print(squares)    #[1, 4, 100, 16, 25]


#lists can be concatenated.
result =  [36, 49, 64, 81, 100]

result.append(200)

print(result)   #[1, 4, 100, 16, 25, 36, 49, 64, 81, 100, 200


# https://docs.python.org/3/tutorial/introduction.html#strings

# strings can be enclosed in single or double quotes



b = eval('test')

print('"Yes," he said.')

print ('doesn\'t')     # use \' to escape the single quote    doesn't

print ("doesn't")       # or use double quote   

print("\"Yes,\" he said.")  # escape double quote

print('C:\some\name')    # C:\some   \n means new line
                         # ame

print(r'C:\some\name')   # use raw strings by adding an r before the first quote C:\some\name

# string literals can span multipel lines, by using triple quotes """...""", or '''...'''



print("""\
Usage: thingy [Options]
    -h              Display this usage message
    -H hostname     Hostname to connect to
""")


# strings can be glued together using the + operator, and repeated with *

newstring = 3 * 'un' + 'ium'    #unununium
print (newstring)

# two or more string literals (the ones enclosed between quotes) next to each other are automatically concatenated.

'Py' 'thon'     # 'Python'
 
# this only works with two literals though, not with variables or expressions
#   prefix = 'Py'
#   prefix 'thon'   # can't concatenate a variable and a string

#this is particular useful when you want to break long strings
text = ('Put several strings with parentheses' 
        ' to have them joined together.')
print(text)  #Put several strings within parentheses to have them joined together.


#Strings can be indexed (subscripted), with the first character having index 0.
#there is no character type; a character is simply a stirng of size one.

word = 'Python'
print(word[0])  # character in position 0   P
print(word[5])  # character in position 5   n

# indices may also be negative numbers, to start counting from the right
# since -0 is the same as 0, negative indices start from -1
print (word[-1])  # last character n
print(word[-2])   # second-last character o
print(word[-6])   # P


# strings support slicing, indexing to obtain individual characters, slicing allws you to obtain substrings

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

print(word[0:2])   # characters from position 0 (included) and 2 (excluded)  Py
print(word[2:5])   #tho

print(word[:2] + word[2:])   # Since the start is always included, and the end always excluded, s[:i] + s[i:] is always equal to sPython

print(word[-2:])  #characters from the second-last (included) to the end


# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1


print(word[42])  # index out of range

#however, out of range slice indexes are gracefully handled when used for slicing
print(word[4:42])  # on
print(word[42:])   # 

#python strings are immutable (can't be changed)

word[0] = '3'  # error

t


a='8'
b=1
a+b
x=a +b
x1=a+ str(1)
'81'

[] list
len(a)
a.append(3)
a[0]
a[1]



# lumnNames = {} defines an empty dict
#columnNames = [] defines an empty list
#dynamically typed



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = []
print(len(letters))

#it is possible to nest list

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

[['a', 'b', 'c'], [1, 2, 3]]
print(x)   #[['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  #['a', 'b', 'c']
print(x[0][1])   #'b'