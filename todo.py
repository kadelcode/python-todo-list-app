import tkinter as tk
from tkinter import messagebox

# File to save tasks
TASKS_FILE = "tasks.txt"

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

# Create GUI Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

# Input field and Add Button
task_entry = tk.Entry(root, width=40) # Create an entry field for the user to type tasks
task_entry.pack(pady=10) # Add some vertical padding

# Create a button labeled "Add Task"
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack() # Display the button

# Run the Application
root.mainloop()