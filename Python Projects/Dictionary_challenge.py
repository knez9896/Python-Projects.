# Create a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)

# Use the get() method on a dictionary
age = my_dict.get("age")
print("Age using get():", age)

# Change a value within a dictionary
my_dict["age"] = 26
print("Dictionary after changing age:", my_dict)

# Add an item to a dictionary
my_dict["profession"] = "Engineer"
print("Dictionary after adding profession:", my_dict)

# Create a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 26},
    "person2": {"name": "Bob", "age": 30},
}
print("Nested dictionary:", nested_dict)

# Use the fromkeys() method on a dictionary
keys = ["name", "age", "city"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print("Dictionary fromkeys():", new_dict)
