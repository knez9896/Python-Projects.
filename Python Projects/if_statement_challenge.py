# Execute an if statement
age = 20
if age >= 18:
    print("You are an adult.")

# Use the elif keyword within an if statement
temperature = 30
if temperature > 35:
    print("It's very hot outside.")
elif temperature > 20:
    print("The weather is nice.")
else:
    print("It's cold outside.")

# Use the else keyword within an if statement
score = 45
if score >= 50:
    print("You passed!")
else:
    print("You failed!")

# Execute a nested if statement
height = 170
if height >= 150:
    if height >= 180:
        print("You are tall.")
    else:
        print("You have average height.")
else:
    print("You are short.")
