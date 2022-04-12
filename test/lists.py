# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ['mango','apple','kiwi' ]
# print(thislist)

# Change the second value by replacing it with two new values:
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ['mango','grapes']
# print(thislist)

# Change the second and third value by replacing it with one value:

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ['mango']
# print(len(thislist))

# The insert() method inserts an item at the specified index:
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1,'mango')
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# Add elements of a tuple to a list:
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# The remove() method removes the specified item.
# thislist = ["apple", "banana", "cherry"]
# thislist.remove('banana')
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# del thislist
# print(thislist)


# The clear() method empties the list.
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i]) 
#     i = i + 1

# thislist = ["apple", "banana", "cherry"]
# newlist = [ x for x in thislist ]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if 'a' in x]
# print(newlist)


# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if x!= 'apple']
# print(newlist)

# Accept only numbers lower than 5:
# newlist = [x for x in range(10) if x<5]
# print(newlist)

# Set the values in the new list to upper case:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)

# Set all values in the new list to 'hello':
# new = ['hello' for x in newlist]
# print(new)

# Return "orange" instead of "banana":
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new = [x if x != 'banana' else 'orange' for x in fruits ]
# print(new)

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# To sort descending, use the keyword argument reverse = True:
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# You can also customize your own function by using the keyword argument key = function.
# def myfunc(n):
#     return abs(n-50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# The reverse() method reverses the current sorting order of the elements.
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# Make a copy of a list with the copy() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# Make a copy of a list with the list() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# lst = list1 + list2
# print(lst)

# for i in list2:
#     list1.append(i)
# print(list1)

list1.extend(list2)
print(list1)