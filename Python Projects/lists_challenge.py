# Create a list
my_list = [1, 2, 3]

# Loop through a list with a for loop
for item in my_list:
    print("Item:", item)

# Use the append() method
my_list.append(4)
print("List after append:", my_list)

# Make a copy of a list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Concatenate two lists
another_list = [5, 6, 7]
concatenated_list = my_list + another_list
print("Concatenated list:", concatenated_list)

# Use the reverse() method on a list
my_list.reverse()
print("Reversed list:", my_list)
