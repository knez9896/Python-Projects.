# Execute a while loop
count = 0
while count < 5:
    print("Count is", count)
    count += 1  

# Use the break statement within a while loop
count = 0
while count < 10:
    if count == 5:
        print("Breaking the loop at count =", count)
        break
    print("Count is", count)
    count += 1

# Use the continue statement within a while loop
count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  
    print("Count is", count)

# Use the else statement within a while loop
count = 0
while count < 5:
    print("Count is", count)
    count += 1
else:
    print("The while loop has ended.")
