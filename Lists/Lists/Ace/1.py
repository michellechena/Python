#naming x-3-2
#1223


print(not '' or not 0 and False )


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make
bake(0, 29)

bake(1, "mashed potatoes")

0 or True # True  # x is false, y, x true x  
not '' or not 0 and False    

true or true and false
true or false

# x is false, x, x true y
13 and False


#http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/

'''

a[start:end]	Start through end -1
a[start : ]	Start through the rest of the array
a[:end]	From the beginning to the end-1
a[ : ] 	Copy the whole array
a[start:end:step]	
a[-1]	Last item
a[-2 :  ]	Last two items
a[ : -2]	Everything except last two items
'''

test = "spam"
b = test[-2:]
test[:-2]

test[-1]

test.reverse()
"maps
#test + str(3)  #spam3


x = -10
print(x % 5)
print(-26 %5)

print(3%5)   # % remainder

3//5   #integer divsion
3/5 #float division

if x > 10:
    print("x>10")
else:
    print("x<=10")

spam="7"
spam=spam + '0'
eggs = int(spam) + 3
print((eggs)) #73
print(float(eggs))


word=input("Enter a word: ")
print(word + ' shop')


x=5
y=x+3
y = int(str(y) + "2")
print(y)


x = 4
x+=5
print(x)

x = 3
num=17
print(num%x)




#73.0
#cheese shop
#82