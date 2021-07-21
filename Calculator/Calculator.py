# Design a Calculator GUI application
# Felix Hirwa Nshuti


# Importing all required Packages
import tkinter as tk
from tkinter import *

"""
Defining the Widget function that is going to be used to create the interface
"""


def create_widgets():
    calculator_display = Entry(root, bd=23, justify="right", font=("Helvetica", 25, "bold"), textvariable=data_val,
                               bg="white")
    calculator_display.grid(row=0, column=0, columnspan=4)
    all_clear = Button(root, text="AC", bd=5, font=("Helvetica", 25, "bold"), width=4, height=2, command=allclearEntry)
    all_clear.grid(row=1, column=0, padx=3, pady=3)

    clear = Button(root, text="C", bd=3, font=("Helvetica", 25, "bold"), width=4, height=2, command=clearEntry)
    clear.grid(row=1, column=1, padx=3, pady=3)

    percentage = Button(root, text='%', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                        command=lambda: click_button('%'))
    percentage.grid(row=1, column=2, padx=3, pady=3)

    d_button = Button(root, text='/', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                      command=lambda: click_button('/'))
    d_button.grid(row=1, column=3, padx=3, pady=3)

    seven = Button(root, text='7', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                   command=lambda: click_button(7))
    seven.grid(row=2, column=0, padx=3, pady=3)

    eight = Button(root, text='8', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                   command=lambda: click_button(8))
    eight.grid(row=2, column=1, padx=3, pady=3)

    nine = Button(root, text='9', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                  command=lambda: click_button(9))
    nine.grid(row=2, column=2, padx=3, pady=3)

    m_button = Button(root, text='*', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                      command=lambda: click_button('*'))
    m_button.grid(row=2, column=3, padx=3, pady=3)

    four = Button(root, text='4', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                  command=lambda: click_button(4))
    four.grid(row=3, column=0, padx=3, pady=3)

    five = Button(root, text='5', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                  command=lambda: click_button(5))
    five.grid(row=3, column=1, padx=3, pady=3)

    four = Button(root, text='6', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                  command=lambda: click_button(6))
    four.grid(row=3, column=2, padx=3, pady=3)

    B_D = Button(root, text='-', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                 command=lambda: click_button('-'))
    B_D.grid(row=3, column=3, padx=3, pady=3)

    one = Button(root, text='1', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                 command=lambda: click_button(1))
    one.grid(row=4, column=0, padx=3, pady=3)

    two = Button(root, text='2', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                 command=lambda: click_button(2))
    two.grid(row=4, column=1, padx=3, pady=3)

    three = Button(root, text='3', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                   command=lambda: click_button(3))
    three.grid(row=4, column=2, padx=3, pady=3)

    a_button = Button(root, text='+', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                      command=lambda: click_button('+'))
    a_button.grid(row=4, column=3, padx=3, pady=3)

    zero = Button(root, text='0', bd=3, font=("Helvetica", 25, "bold"), width=10, height=2,
                  command=lambda: click_button(0))
    zero.grid(row=5, column=0, padx=3, pady=10, columnspan=2)

    decimal_point = Button(root, text='.', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                           command=lambda: click_button('.'))
    decimal_point.grid(row=5, column=2, padx=3, pady=10)

    equal_button = Button(root, text='=', bd=3, font=("Helvetica", 25, "bold"), width=4, height=2,
                          command=calculateResult)
    equal_button.grid(row=5, column=3, padx=3, pady=10)


c_val = 0


# Defining click_button function for getting the user pressed button
def click_button(in_val):
    global c_val
    # storing the c_val according to the button value user pressed
    c_val += str(in_val)
    # Setting the Entry Widget value
    data_val.set(c_val)


# Saving the result
def calculateResult():
    global c_val
    # eval() run python expression within it and parses the value fed to it
    result = str(eval(c_val))
    # Setting the Entry Widget value to that of the result variable's value
    data_val.set(result)


# Clearing all function
def allclearEntry():
    global c_val
    # resetting the c_val value by making an empty string to be displayed on the Widget
    c_val = ""
    data_val.set(c_val)


# Entry Clearing
def clearEntry():
    # Declaring global variables for our operation
    global c_val, data_val
    # deleting the last typed character in the Widget
    val_clear = data_val.get()[:-1]
    # Setting back the variables to cleared ones
    c_val = val_clear
    data_val.set(c_val)


# Creating object root of tk
root = tk.Tk()

# Title and size of the interface
root.title('Felix Calculator')
root.resizable(True, False)
root.configure(background='gray79')

# Creating tkinter variable
data_val = StringVar()
c_val = ""
create_widgets()

# Making the operation not enabled
root.mainloop()
