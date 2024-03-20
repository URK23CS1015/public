import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        result_label.config(text = "Result: " + str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Calculator")

tk.Label(root, text="Calculator", font=("Arial", 20)).grid(row=0, column=0, columnspan=4)

tk.Label(root, text="Type Value 1:").grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

tk.Label(root, text="Type Value 2:").grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

tk.Button(root, text="+", command=lambda: calculate('+'), bg='green').grid(row=3, column=0)
tk.Button(root, text="-", command=lambda: calculate('-'), bg='green').grid(row=3, column=1)
tk.Button(root, text="*", command=lambda: calculate('*'), bg='green').grid(row=3, column=2)
tk.Button(root, text="/", command=lambda: calculate('/'), bg='green').grid(row=3, column=3)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=4)

root.mainloop()