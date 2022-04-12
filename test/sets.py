# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# Check if "banana" is present in the set:
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

# Add an item to a set, using the add() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.add('mango')
# print(thisset)


# To add items from another set into the current set, use the update() method.
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# To remove an item in a set, use the remove(), or the discard() method.
# thisset = {"apple", "banana", "cherry"}
# thisset.remove('banana')
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)


# The clear() method empties the set:
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)


# The del keyword deletes the set completly:
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)


# The union() method returns a new set with all items from both sets:
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)