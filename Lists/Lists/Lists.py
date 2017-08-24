#https://docs.python.org/3/tutorial/introduction.html#lists

#list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]

print(squares)

#lists can be indexed and sliced.
#All slice operations return a new list containing the requested elements


print(squares[-3:])


#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

squares[-3] = 100
print(squares)    #[1, 4, 100, 16, 25]


#lists can be concatenated.
result = squares + [36, 49, 64, 81, 100]

result.append(200)

print(result)   #[1, 4, 100, 16, 25, 36, 49, 64, 81, 100, 200

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] = ['C', 'D', 'E']

print(letters)  #['a', 'b', 'C', 'D', 'E', 'f', 'g']

letters[2:5] = []
print(letters)  #['a', 'b',  'f', 'g']

print(len(letters))  #4

#it is possible to nest list

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)   #[['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  #['a', 'b', 'c']
print(x[0][1])   #'b'