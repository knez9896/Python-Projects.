# Execute a for loop
for i in range(5):
    print("i is", i)

# Use the break statement within a for loop
for i in range(10):
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    print("i is", i)

# Use the continue statement within a for loop
for i in range(10):
    if i == 4:
        continue  # Skip printing when i is 4
    print("i is", i)

# Use the range() function within a for loop
for i in range(2, 10, 2):  
    print("i is", i)

# Use the else keyword within a for loop
for i in range(5):
    print("i is", i)
else:
    print("The for loop has completed without a break.")
