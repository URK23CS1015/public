import tkinter as tk
from tkinter import messagebox

def submit():
    print("Form Submitted")
    # Add your form submission code here

root = tk.Tk()
root.title("Registration Form")

tk.Label(root, text="Registration Form", font=("Arial", 20)).grid(row=0, column=0, columnspan=2)

tk.Label(root, text="Full Name:").grid(row=1, column=0)
fullname = tk.Entry(root)
fullname.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email = tk.Entry(root)
email.grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
gender = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=3, column=1)
tk.Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=3, column=2)

tk.Label(root, text="Country:").grid(row=4, column=0)
country = tk.StringVar()
country.set("Select Country") # default value
tk.OptionMenu(root, country, "India", "USA", "UK", "Australia").grid(row=4, column=1)

tk.Label(root, text="Programming:").grid(row=5, column=0)
java = tk.IntVar()
python = tk.IntVar()
tk.Checkbutton(root, text="Java", variable=java).grid(row=5, column=1)
tk.Checkbutton(root, text="Python", variable=python).grid(row=5, column=2)

tk.Button(root, text="Submit", command=submit, bg='red').grid(row=6, column=0, columnspan=2)

root.mainloop()
