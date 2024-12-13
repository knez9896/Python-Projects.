import sqlite3

# File list provided for the assignment
fileList = ('informatio.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Function to create a database and insert .txt files
def create_database():
    # Connect to SQLite database (creates the database if it doesn't exist)
    conn = sqlite3.connect('file_database.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist already
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL
        )
    ''')

    # Filter the file list to include only .txt files
    txt_files = [file for file in fileList if file.endswith('.txt')]

    # Insert qualifying files into the database
    for file in txt_files:
        cursor.execute('INSERT INTO files (filename) VALUES (?)', (file,))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    # Print the qualifying .txt files
    print("Qualifying .txt files added to the database:")
    for file in txt_files:
        print(file)

# Main execution point
if __name__ == "__main__":
    create_database()
