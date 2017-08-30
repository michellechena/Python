'''
>>> (True and (not False)) or ((not True) and False)
This is because boolean operators, like arithmetic operators, have an order of operation:
not has the highest priority
and
or has the lowest priority
It turns out and and or work on more than just booleans (True, False). 
Python values such as 0, None, '' (the empty string), and [] (the empty list) 
are considered false values. All other values are considered true values.
'''

'''
Python Boolean operators return the last value evaluated, not True/False. The docs have a good explanation of this:
The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
'''

y = 'eggs' and '' and 5  
x = 0 or 4 and 2 or 7
input()
