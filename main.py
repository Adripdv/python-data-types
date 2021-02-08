'''Strings''' 
# s = 'This is a single line string'
# print(s)
# print(type(s))

# s = '''This is a multiline 
# string example'''
# print(s)

#=================================================
# Find a character by index 

# s = 'string sample'
# print(s[9])


#=================================================
# Slicing

# s = 'string sample'
# print(s[5:]) 
# print(s[1:8]) # slice from index '1' to the position '6'

#=================================================
# immutable 

# s = 'string sample'
# s[2] = 'o'
# print(s) # TypeError: 'str' object does not support item assignment

'''Numeric Type (integer, Float, Complex)'''

# x = 1334589725654
# print(type(x))

# Accurate up to 15-16 decimal places 
# x = 0.1234569874578965645689
# print(type(x))
# print (x)

# x = 1+2j
# print(type(x))

'''Sequence types (List, Tuple, Range)'''

# #List 
# #homogeneous 
# x = [] #empety list 
# x = [10, 2.5, 'hello']
# print(x[0])
# print(x[1:3]) # slice list items from position 1(2.5) to position 3 'hello'

# # mutable

# x[2] = 'Python' # find list item on position 2 'hello' and change for 'Python'
# print(x)

#=================================================

#Tuple 
#heterogeneous

# tuple = () #empety tuple

# Both examples bellow with the comma are type tuples, without the comma it makes it a string.
# tuple = 'hello',  
# tuple = ('hello',)

# tuple = 'hello'  
# tuple = ('hello') 

#=================================================
# tuple = ("cat", [4,2,3], (1,2,3))
# print(type(tuple))
# print(tuple[0])

# print(type([3])) #To comment result with Kingsley
# print(type[3]) #TypeError: 'type' object is not subscriptable

#=================================================

#immutable
# tuple = ("cat", [4,2,3], (1,2,3))
# tuple[2] = 10
# print(tuple) #TypeError: 'tuple' object does not support item assignment

#=================================================

#Range
# x = range(10) # 0 to 9 
# for n in x:
#   print(n) 

''' Mapping type (Dictionary)'''

# dict = {}
# print(type(dict))

#=================================================

# dict = {'name':'Adriana', 'age': 40}
# print(dict['name'])
# print(dict.get('age')) 

# #mutable
# dict['age'] = 26
# print(dict)

'''Set Types (it only has single values)'''

# set = {} # empty dict 
# print(type(set))

# x = {} 
# print(type(x))

# z = set()
# print(type(z))

#=================================================

# y = {3.2, "hi" (1, 2,3)}
# print(type(y))
# print(y[0]) # TypeError: 'str' object is not callable


#=================================================

# set = {3.2, "hi", (1,2,3), "hi"}
# print(set) # does print call duplicated values

#=================================================
# cannot have mutable lists as bellow e.g. [1,2,3] in a set 

# set = {3.2, "hi", (1,2,3), [1,2,3]} #TypeError: unhashable type: 'list'
# print(set)

'''Boolean Type (True or False)'''

# print(type(True))
# print(type(False))

# #boolean as numbers
# print(True == 1)
# print(False == 0)

# #interesting logic
# print(True + True) # same as 1 +1 as True is equal to 1

# #not boolean operator 
# print(not True)
# print(not False)

# #and boolean operator (as long as False exists it's always going to be False, only the abscence of False is True (true poetry :-))
# print(True and False) 
# print(True and True)
# print(False and False) 

# #or boolean operator (as long as there is True is True (pure poetry again :-))
# print(True or False)
# print(True or True)
# print(False or True)
# print(False or False)