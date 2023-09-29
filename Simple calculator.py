import tkinter as tk
from tkinter import messagebox
import math
# Function to perform arithmetic operations
def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        elif operation == 'sqrt':
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                messagebox.showerror("Error", "Square root of a negative number is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        result_label.config(text=f"Result: {result:.2f}")
        calculation_history.insert(tk.END, f"{num1} {operation} {num2} = {result:.2f}\n")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to clear the calculation history
def clear_history():
    calculation_history.delete(1.0, tk.END)
# Create the main window
root = tk.Tk()
root.title("Complex Calculator")
# Set window size and center it on the screen
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Configure the calculator's appearance
root.configure(bg="lightgray")
# Create input fields
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
# Create operation dropdown
operations = ['+', '-', '*', '/', 'sqrt']
operation_var = tk.StringVar()
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
# Create Calculate button
calculate_button = tk.Button(root, text="Calculate", command=perform_calculation, bg="green", fg="white", cursor="hand2")
# Create result label
result_label = tk.Label(root, text="Result: ", bg="lightgray")
# Create calculation history box
calculation_history = tk.Text(root, height=5, width=40)
# Create Clear History button
clear_history_button = tk.Button(root, text="Clear History", command=clear_history, bg="red", fg="white", cursor="hand2")
# Grid layout
entry_num1.grid(row=0, column=0, padx=10, pady=10)
operation_menu.grid(row=0, column=1, padx=10, pady=10)
entry_num2.grid(row=0, column=2, padx=10, pady=10)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
calculation_history.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
clear_history_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
# Run the main loop
root.mainloop()