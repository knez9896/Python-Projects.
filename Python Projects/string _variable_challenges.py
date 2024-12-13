myString = "hello world"
print(myString)

# Length of the string
print(len(myString))

# Slice syntax
print(myString[0:5])  # 'hello'

# Accessing individual characters
print(myString[0])  # 'h'
print(myString[1])  # 'e'

# String concatenation
fName = "Daniel"
lName = "Christie"
print(fName + lName)  # 'DanielChristie'
print(fName + " " + lName)  # 'Daniel Christie'

# Using format()
print("Hello {} {}, welcome to Python!".format(fName, lName))

# Multiline string
multi_line_string = """This is a multiline string.
It spans multiple lines."""
print(multi_line_string)

# Strip method
stripped_string = "   hello   ".strip()
print(stripped_string)  # 'hello'

# Upper method
print(myString.upper())  # 'HELLO WORLD'

# Escape character
escaped_string = "He said, \"Python is fun!\""
print(escaped_string)

# Using 'in' or 'not in'
print("world" in myString)  # True
print("Python" not in myString)  # True
_
