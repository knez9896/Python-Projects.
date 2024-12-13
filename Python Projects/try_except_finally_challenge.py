try:
    
    result = 10 / 0
except ZeroDivisionError as e:
    
    print("Error: Cannot divide by zero!")
    print("Exception message:", e)
finally:
    
    print("This block will always run.")
