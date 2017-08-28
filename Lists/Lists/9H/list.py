[] empty list
{} empty dict
() empty tuple
(1, 3)
a = [ 1, 3, 3]   
a[0] =2
[2, 3, 3]

b= (1,3,4)
b[1]=3

'''
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
'''
i = 0
a=[1,3,5,9,11]
while i < len(a):
    print (a[i])
    i = i + 3

list = ['larry', 'curly','curly', 'moe']
list.append('shemp') ## append elem at end
list.insert(0, 'xxx')## insert elem at index 0
list.extend(['yyy', 'zzz'])## add list of elems at end
print(list)## ['xxx', 'larry', 'curly','curly', 'moe', 'shemp', 'yyy', 'zzz']
print('index')
print(list.index('curly'))## 2
list.remove('curly') ## search and remove that elemen
list.pop(2) ## removes and returns 'larry'
print(list)## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
    print(sum)

list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay')
