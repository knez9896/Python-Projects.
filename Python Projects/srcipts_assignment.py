import os
from datetime import datetime

def list_txt_files(directory):
    try:
        # Get all files in the specified directory
        files = os.listdir(directory)
        
        print(f"Listing .txt files in directory: {directory}\n")
        
        for file in files:
            # Form the full path
            full_path = os.path.join(directory, file)
            
            # Check if it's a file and ends with .txt
            if os.path.isfile(full_path) and file.endswith('.txt'):
                # Get the modified time
                modified_time = os.path.getmtime(full_path)
                readable_time = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
                
                # Print the file name and modified time
                print(f"{file} - Last Modified: {readable_time}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory to check
directory_to_check = input("Enter the directory path to scan: ")
list_txt_files(directory_to_check)
