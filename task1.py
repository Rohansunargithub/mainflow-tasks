#Write a python program to create a list, a dictionary, and a set. Perform basic operations like adding, removing, and modifying elements.

# Creating and modifying a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Adding an element to the list
#Adding: The append() method adds an element to the end of the list.
my_list.append(6)
print("List after adding 6:", my_list)

# Removing an element from the list
#Removing: The remove() method removes the first occurrence of a value.
my_list.remove(3)
print("List after removing 3:", my_list)

# Modifying an element in the list
#Modifying: Direct indexing is used to change an element.
my_list[1] = 10
print("List after modifying second element to 10:", my_list)

# Creating and modifying a dictionary
my_dict = {'name': 'Alice', 'age': 30}
print("Original Dictionary:", my_dict)

# Adding an element to the dictionary
#Adding: A new key-value pair is added.
my_dict['city'] = 'New York'
print("Dictionary after adding 'city':", my_dict)

# Removing an element from the dictionary
#Removing: The del statement is used to remove a key-value pair.
del my_dict['age']
print("Dictionary after removing 'age':", my_dict)

# Modifying an element in the dictionary
#Modifying: Direct indexing is used to change the value associated with a key.
my_dict['name'] = 'Bob'
print("Dictionary after modifying 'name' to 'Bob':", my_dict)

# Creating and modifying a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding an element to the set
#Adding: The add() method adds an element to the set.
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing an element from the set
#Removing: The remove() method removes an element (raises an error if the element is not found). discard() is used here as an alternative, which doesn't raise an error.
my_set.remove(2)
print("Set after removing 2:", my_set)

# Sets do not support indexing, so we cannot modify an element directly
# We will demonstrate this by adding and removing elements to reflect changes
my_set.discard(3)  # discard doesn't raise an error if the element is not present
print("Set after discarding 3:", my_set)

# Adding a new element (since we can't modify an element directly)
#Modification: Sets are unordered, so you can't modify an element directly. Instead, you can add or remove elements to reflect changes.
my_set.add(10)
print("Set after adding 10:", my_set)
