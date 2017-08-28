#naming x-3-2
#1223
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
test*3


test+ str(3)  #spam3


x = -10
print(x % 5)
print(-26 %5)

print(3%5)

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