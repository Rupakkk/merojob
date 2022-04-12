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





