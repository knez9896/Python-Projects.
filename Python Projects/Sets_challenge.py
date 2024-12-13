# Create a set
my_set = {1, 2, 3}
print("Set:", my_set)

# Add an item to a set using the add() method
my_set.add(4)
print("Set after adding 4:", my_set)

# Use the remove() method to take an item out of a set
my_set.remove(2)
print("Set after removing 2:", my_set)

# Use the difference() method on a set
another_set = {3, 4, 5}
difference_set = my_set.difference(another_set)
print("Difference of sets (my_set - another_set):", difference_set)
