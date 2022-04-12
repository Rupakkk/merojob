# Duplicate values will overwrite existing values:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict.get('brand'))
# print(thisdict.keys())
# print(thisdict.values())


# Add a new item to the original dictionary, and see that the keys list gets updated as well:
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# y = car.values()
# z = car.items()
# print(x,y,z) before the change
# car["color"] = "white"
# print(x,y,z) after the change


# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({'country':'Nepal'})
# print(thisdict)
# thatdict = {'city':'ktm'}
# thisdict.update(thatdict)
# print(thisdict)


# Removing Items
# There are several methods to remove items from a dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del(thisdict['brand'])
# print(thisdict)
# thisdict.pop('model')
# print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# The del keyword can also delete the dictionary completely:

# The clear() method empties the dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)
# mydict = dict(thisdict)
# print(mydict)