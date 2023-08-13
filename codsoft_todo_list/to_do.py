import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = tasks_list.curselection()
    if selected_task_index:
        tasks_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    tasks_list.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create and configure widgets
task_entry = tk.Entry(app, width=30)
add_button = tk.Button(app, text="Add Task", command=add_task)
delete_button = tk.Button(app, text="delete Task", command=delete_task)
clear_button = tk.Button(app, text="Clear All", command=clear_tasks)
tasks_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40)

# Place widgets on the window
task_entry.pack(pady=10)
add_button.pack()
delete_button.pack()
clear_button.pack()
tasks_list.pack(pady=10)

# Start the main loop
app.mainloop()
