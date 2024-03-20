from tkinter import *

def calculate(operator):
    num1 = val1.get()
    num2 = val2.get()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0: 
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    Textbox_result.delete(0, END)
    Textbox_result.insert(0, result)

root = Tk()
root.geometry("400x300")
root.title("URK23CS1028")
root.configure(bg='grey')  # Set root window background color to grey

l = Label(root, text='Calculator', font=('Calibri', 14), fg='black', bg='grey')
l.place(x=155, y=30)

l1 = Label(root, text='Type Value 1', bg='grey', font=('Calibri', 10))
l1.place(x=100, y=70)

val1 = IntVar()
val2 = IntVar()

Entry_value1 = Entry(root, textvariable=val1, width=20)
Entry_value1.place(x=200, y=70)
Entry_value1.delete(0,END)
l2 = Label(root, text='Type Value 2', bg='grey', font=('Calibri', 10))
l2.place(x=100, y=100)

Entry_value2 = Entry(root, textvariable=val2, width=20)
Entry_value2.delete(0,END)
Entry_value2.place(x=200, y=100)

Button_add = Button(root, text='+', bg='green', fg='white', width=5, command=lambda: calculate('+'))
Button_add.place(x=100, y=130)

Button_subtract = Button(root, text='-', bg='green', fg='white', width=5, command=lambda: calculate('-'))
Button_subtract.place(x=150, y=130)

Button_multiply = Button(root, text='*', bg='green', fg='white', width=5, command=lambda: calculate('*'))
Button_multiply.place(x=200, y=130)

Button_divide = Button(root, text='/', bg='green', fg='white', width=5, command=lambda: calculate('/'))
Button_divide.place(x=250, y=130)

l3 = Label(root, text='Result:', bg='grey', font=('Calibri', 10))
l3.place(x=100, y=200)

Textbox_result = Entry(root, width=20)
Textbox_result.place(x=150, y=200)

root.mainloop()