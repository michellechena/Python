#http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/#Program1DLife

'''
Unlike C or C++, Python's modulo operator (%) always return a number having the same 
sign as the denominator (divisor). Your expression yields 3 because
(-5) % 4 = (-2 × 4 + 3) % 4 = 3.


-5 % 11 , simply add 11 to -5 until you obtain a positive integer in the range [0,10] , 
and the result is 6.
'''

-2 ** 3 + 7

def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin

whats_on_the_telly(['test'])

y= - 3 % 5
x = -3 % 5 - 8

'''
26 % 7 (you will get remainder)
26 / 7 (you will get divisor can be float value )
26 // 7 (you will get divisor only integer value) )
'''

'spam' * 3 + 'lovely spam'
print('spam' + 3 + 'lovely spam')

'eggs' and '' and 5
0 or 4 and 2 or 7

input()


#  {} dicticnary
# [] list
x = 'hello' #string 
len(x)
food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
food["spam"] = "yes"

food = {'egg': 'yes', 'ham': 'yes', 'spam': 'yes'}

for key in food:
    print(key)


#https://stackoverflow.com/questions/20510768/python-count-frequency-of-words-in-a-list

 words = file("test.txt", "r").read().split() #read the words into a list.
uniqWords = sorted(set(words)) #remove duplicate words and sort
for word in uniqWords:
    print(words.count(word), word)

#http://www.python-course.eu/dictionaries.php
w={"house":"Haus","cat":"Katze","red":"rot"}
w.items()
[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
w.keys()
['house', 'red', 'cat']
w.values()
['Haus', 'rot', 'Katze']



if input == 'a':
    for char in 'abc':
        if char in some_list:
            some_list.remove(char)


#Write two versions of a Python function named mystery that has the following behaviour.
## In the first version, use a loop to construct the result. In the second version, do not use any loops.


def mystery(n, word):
    result = ''
    while len(result) < n:
        result += word
    return result[:n]


mystery(15, 'red')
#'redredredredred'
mystery(12, 'green')
#'greengreengr'
mystery(26, 'aquamarine')
#'aquamarineaquamarineaquama'

def mystery(n, word):
    return (word*n)[:n]