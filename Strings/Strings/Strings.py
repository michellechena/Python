
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