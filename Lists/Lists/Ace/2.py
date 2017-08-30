
#https://www.programiz.com/python-programming/dictionary

#https://www.testdome.com/testing/sample/5214

a = [1, 2, 3]
a.reverse()
print(a)

9/3 #float division
11//3 #integer division
11%3  #remainder

1 and 4  #if x false, returns x, else returns y
0 or 4  #if x false, returns y, else returns x

1 or 4
1 and 4  
0 and 4


a = [1, 2, 3]
a.reverse()
print(a)
b = a[::-1]   #a content does not change.   returns a new list
print(a)
print(b)      #b the resulting b contains reverse-ordered a

#fix the bug
class MathUtils:
    @staticmethod
    def average(a, b):
        return (a + b) / 2       #bug: needs (a + b). order of precedence

print(MathUtils.average(2, 1))



'''
implement a group_by_owners function that: 
1. accepts a dictionary containing the file owner name for each file
2. returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'input.txt': 'Randy', 'Code.py':'Stan', 'Output.txt':'Randy'} 
the group_by_owners function should return {'Randy':['input.txt','output.txt'], 'Stan':['Code.py']}.
'''
#{'input.txt': 'Randy', 'Code.py':'Stan', 'Output.txt':'Randy'}
files.items() # [('input.txt', 'randy'), ('code.py','stan'), ('output.txt', 'randy')]
files.keys() #['input.txt', 'copy.py', 'output.txt']
files.values() #['randy', 'stan', 'randy']

indexing, slicing, 
class FileOwners:
    @staticmethod
    def group_by_owners(files):
        result = {}   #empty dictionary
        for file, owner in files.items():    #key value pair
            result[owner] = result.get(owner,[]) + [file]
        return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(FileOwners.group_by_owners(files)) 


#character case can be ignored.  so Tet is a palindrom of TET
class Palindrome:
    @classmethod
    def is_palindrome(word):
        return word.lower()[::-1] == word.lower()
        
print(Palindrome.is_palindrome('Deleveled'))


