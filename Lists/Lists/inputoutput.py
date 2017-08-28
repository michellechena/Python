#tup1 = (12, 34.56);
#tup2 = ('abc', 'xyz');

#print(tup1[0])
#print(tup2[1])


#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#print ("dict['Name']: ", dict['Name'])
#print ("dict['Age']: ", dict['Age'])
#print("dict['Class']:", dict['Class'])


##updating dictionary
#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#dict['Age'] = 8; # update existing entry
#dict['School'] = "DPS School"; # Add new entry


#print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['School'])

#print(dict)

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#del dict['Name']; # remove entry with key 'Name'
#dict.clear();     # remove all entries in dict
#del dict ;        # delete entire dictionary




dict = {'Name': 'Zara', 'Age': 7}

print(dict.items())
print(dict.keys())

def printme(str):
    print(str)
    return

printme('test')


# Function definition is here
def changeme( mylist ):
   #"This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print( "Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))


total = 10; # This is global variable.
# Function definition is here

def sum( arg1, arg2 ):
   total=5
   print( "Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total )


Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print (Money)
AddMoney()
print (Money)


import math

content = dir(math)

print (content)

str = input("Enter your input: ");
print ("Received input is : ", str)


# Open a file
fo = open("factor.py" ,"r+")
str = fo.read(100);
print( "Read String is : ", str)

# Check current position
position = fo.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print ("Again read String is : ", str)
# Close opend file
fo.close()