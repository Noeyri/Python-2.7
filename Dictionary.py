# Python Dictionaries

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:


# Ejemplo
# Cree e imprima un diccionario:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])



# Dictionary Items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])



# Duplicates Not Allowed

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)



# Dictionary Length

# To determine how many items a dictionary has, use the len() function:
# print(len(thisdict))



# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# Example
# String, int, boolean, and list data types:

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }



# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
# <class 'dict'>

# Example
# Print the data type of a dictionary:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# "List" is a collection which is ordered and changeable. Allows duplicate members.
#
# "Tuple" is a collection which is ordered and unchangeable. Allows duplicate members.
#
# "Set" is a collection which is unordered and unindexed. No duplicate members.
#
# "Dictionary" is a collection which is unordered and changeable. No duplicate members.
#
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for
# a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.