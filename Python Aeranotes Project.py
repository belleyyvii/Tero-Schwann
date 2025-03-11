import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("aeranotes_tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

# Function to load tasks from a file on startup
def load_tasks():
    try:
        with open("aeranotes_tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Creating the main window
root = tk.Tk()
root.title("AeraNotes - To-Do List")
root.geometry("400x500")

# Creating task entry field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Creating buttons and linking them to functions
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

# Creating listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Load tasks from file when the application starts
load_tasks()

# Run the main event loop
root.mainloop()
