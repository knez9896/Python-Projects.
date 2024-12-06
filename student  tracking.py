import sqlite3
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END, messagebox

# Database setup
def setup_database():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    phone TEXT,
                    email TEXT,
                    course TEXT
                 )''')
    conn.commit()
    conn.close()

# Add student
def add_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    course = course_entry.get()

    if not (first_name and last_name and phone and email and course):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (first_name, last_name, phone, email, course) VALUES (?, ?, ?, ?, ?)",
              (first_name, last_name, phone, email, course))
    conn.commit()
    conn.close()

    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    course_entry.delete(0, END)

    load_students()

# Load students into the listbox
def load_students():
    student_list.delete(0, END)
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    for row in c.fetchall():
        student_list.insert(END, f"{row[0]} | {row[1]} {row[2]} | {row[3]} | {row[4]} | {row[5]}")
    conn.close()

# Delete selected student
def delete_student():
    selected = student_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No student selected!")
        return

    student_id = student_list.get(selected[0]).split(" | ")[0]
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

    load_students()

# GUI setup
root = Tk()
root.title("Student Tracking")

# Labels and Entry Fields
Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=5)
first_name_entry = Entry(root)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
last_name_entry = Entry(root)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Phone Number").grid(row=2, column=0, padx=10, pady=5)
phone_entry = Entry(root)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Email").grid(row=3, column=0, padx=10, pady=5)
email_entry = Entry(root)
email_entry.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Current Course").grid(row=4, column=0, padx=10, pady=5)
course_entry = Entry(root)
course_entry.grid(row=4, column=1, padx=10, pady=5)

Button(root, text="Submit", command=add_student).grid(row=5, column=0, columnspan=2, pady=10)

# Student List
Label(root, text="Student List").grid(row=6, column=0, columnspan=2, pady=5)
scrollbar = Scrollbar(root)
scrollbar.grid(row=7, column=2, sticky="ns")

student_list = Listbox(root, width=80, yscrollcommand=scrollbar.set)
student_list.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
scrollbar.config(command=student_list.yview)

Button(root, text="Delete", command=delete_student).grid(row=8, column=0, columnspan=2, pady=10)

# Initialize database and load data
setup_database()
load_students()

root.mainloop()
