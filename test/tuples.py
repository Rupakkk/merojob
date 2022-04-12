# One item tuple, remember the comma
# thistuple = ('apple',)
# print(thistuple)


#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# Print the second item in the tuple:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])


# thistuple = ("apple", "banana", "cherry")
# if 'apple' in thistuple:
#     print('yes')


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = 'kiwi'
# x = tuple(y)
# print(x)

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
# thistuple = ("apple", "banana", "cherry")
# tups = ('mango',)
# thistuple += tups
# print(thistuple)

# in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# fruits = ("apple", "banana", "cherry")
# (a,b,c) = fruits
# print(a)
# print(b)
# print(c)

# fruits = ["apple", "banana", "cherry"]  Unpacking a list
# [a,b,c] = fruits
# print(a)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (a,b,*c) = fruits
# print(a)
# print(b)
# print(c)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (a,*b ,c,d) = fruits
# print(a)
# print(b)
# print(c)


# Multiply Tuples
# tuple1 = ("a", "b" , "c")
# tuple2 = tuple1 * 3
# print(tuple2)
# print(tuple1.count('a'))
# print(tuple2.index('b'))

