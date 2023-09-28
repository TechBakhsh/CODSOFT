import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
from tkcalendar import Calendar
# Start the to-do list
todo_list = []
# Function to add a task
def add_task():
    task_text = entry.get()
    due_date_text = due_date_entry.get()
    if task_text:
        task = {
            "task": task_text,
            "due_date": due_date_text if due_date_text else "No Due Date",
            "completed": False
        }
        todo_list.append(task)
        update_listbox()
        entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to update a task
def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        updated_task_text = entry.get()
        updated_due_date_text = due_date_entry.get()
        if updated_task_text:
            selected_task_index = selected_task_index[0]
            selected_task = todo_list[selected_task_index]
            selected_task["task"] = updated_task_text
            selected_task["due_date"] = updated_due_date_text if updated_due_date_text else "No Due Date"
            update_listbox()
            entry.delete(0, tk.END)
            due_date_entry.delete(0, tk.END)
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to mark a task as completed
def mark_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        selected_task = todo_list[selected_task_index]
        selected_task["completed"] = True
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Function to delete a task
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        del todo_list[selected_task_index]
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to save tasks to a file
def save_tasks():
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

# Function to load tasks from a file
def load_tasks():
    try:
        with open("todo_list.json", "r") as file:
            loaded_tasks = json.load(file)
            for task in loaded_tasks:
                todo_list.append(task)
            update_listbox()
    except FileNotFoundError:
        pass

# Function to update the listbox with tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for task in todo_list:
        task_text = task["task"]
        due_date_text = task["due_date"]
        completed = task["completed"]
        if completed:
            listbox.insert(tk.END, f"[X] {task_text} (Due: {due_date_text})")
        else:
            listbox.insert(tk.END, f"[ ] {task_text} (Due: {due_date_text})")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Change the background color of the root window
root.configure(bg="lightblue")

# Create and configure the entry widget
entry = tk.Entry(root, width=40)
#entry = tk.Label(root, text="Enter something:")

label = tk.Label(root, text="Enter Your Task:")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()
# Create and configure the due date entry widget
due_date_label = tk.Label(root, text="Due Date (optional):", fg="blue")
due_date_label.pack()
due_date_entry = tk.Entry(root, width=20)
due_date_entry.pack(pady=5)
# Create and configure the listbox widget
listbox = tk.Listbox(root, width=40, bg="lightgray",fg="green")
listbox.pack()

# Load tasks from file (if available)
load_tasks()
# Define a function to change the background color when the mouse hovers over the button.
def on_hover(event):
    event.widget.config(bg="lightyellow")
    # Define a function to change the background color back to the original color when the mouse leaves the button.
def on_leave(event):
    event.widget.config(bg=event.widget.default_bg_color)
# Create buttons for adding, updating, marking as completed, and deleting tasks, and add bg color
add_button = tk.Button(root, text="Add Task", command=add_task, width=15, bg="lightgreen", relief=tk.RAISED, cursor="hand2", borderwidth=3)
update_button = tk.Button(root, text="Update Task", command=update_task, width=15, bg="lightblue", relief=tk.RAISED, cursor="hand2", borderwidth=3)
complete_button = tk.Button(root, text="Mark as Completed", command=mark_completed, width=15, bg="lightgray", relief=tk.RAISED, cursor="hand2", borderwidth=3)
delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=15, bg="lightcoral", relief=tk.RAISED, cursor="hand2", borderwidth=3)
 #Store the default background color for each button.
add_button.default_bg_color = "lightgreen"
update_button.default_bg_color = "lightblue"
complete_button.default_bg_color = "lightgray"
delete_button.default_bg_color = "lightcoral"

# Bind hover and leave events to the buttons.
add_button.bind("<Enter>", on_hover)
add_button.bind("<Leave>", on_leave)
update_button.bind("<Enter>", on_hover)
update_button.bind("<Leave>", on_leave)
complete_button.bind("<Enter>", on_hover)
complete_button.bind("<Leave>", on_leave)
delete_button.bind("<Enter>", on_hover)
delete_button.bind("<Leave>", on_leave)
# pack button
add_button.pack()
update_button.pack()
complete_button.pack()
delete_button.pack()
# Start the Tkinter main loop
root.mainloop()