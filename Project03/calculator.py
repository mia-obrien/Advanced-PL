# /*****************************************************************************
# *                    
# *  Authors:           Mia, Lelia, Deangelo
# * 
# *  Label:            CMPS 5113 Advanced Programming Languages Project 3 – OOP
# *  Title:            The Interactive Calculator
# *  Course:           CMPS 5113 Advanced Programming Languages
# *  Semester:         Fall 2021
# * 
# *  Description:
# *        This program provides the user an interactive calculator 
# * 
# *  Usage:
# *        Use the operators and operands
# * 
# * 
# *****************************************************************************/

#Import the tkinter library to make the GUI and math library for the operations
from tkinter import *
import math
from math import sin, cos, tan, factorial, sqrt, log
from typing import Container



fact = factorial
# /**
#  * Class Name: Calculator
#  *        
#  * Description:
#  *      This class creates buttons for the GUI and provides math operations for the user
#  * 
#  * Public Methods:
#  *      - button_font
#  *      - entry_font
#  *      - parent
#         - button_width
#         - button_height
#         - container
#         - container.grid
#         - string
#         - display
#  * 
#  * Private Methods:
#  *      -  entry(self, x_, y_)
#  *      -  button(self, char_, x_, y_)
#  *      -  button_eq(self, char_, x_, y_)
#  *      -  button_clear(self, char_, x_, y_)
#  *      -  button_eq(self, char_, x_, y_)
#  *      -  button_clear(self, char_, x_, y_)
#  *      -  button_rem(self, char_, x_, y_)
#  *      -  button_show(self, char_, x_, y_)
#  *      -  button_help(self, char_, x_, y_)
#  *
#  * Usage: 
#  * 
#  *      - It has basic GUI and shows the operands and operators in the window
#  *      
#  */
class Calculator:
    def __init__(self, parent, x, y):
        self.button_font = ('Times', 1)
        self.entry_font = ('Times', 30)
        self.parent = parent

        self.button_width = 4
        self.button_height = 1
        self.container = Frame(self.parent)
        self.container.grid(row=x, column=y)

        self.string = ''

        self.entry(0, 0)

        self.button('7', 2, 2)
        self.button('8', 2, 3)
        self.button('9', 2, 4)

        self.button('4', 3, 2)
        self.button('5', 3, 3)
        self.button('6', 3, 4)

        self.button('1', 4, 2)
        self.button('2', 4, 3)
        self.button('3', 4, 4)

        self.button('0', 5, 2)

        self.button('+', 5, 5)
        self.button('-', 4, 5)
        self.button('*', 3, 5)
        self.button('/', 2, 5)

        self.button('(', 1, 0)
        self.button(')', 1, 1)

        self.button_eq('=', 5, 3)

        self.button_clear('AC', 1, 2)
        self.button_rem('<', 1, 3)
        self.button(".",5,0)
        self.button('%',5,1)
        self.button('log',2,0)
        self.button('fact',2,1)
        self.button('sqrt',3,0)
        self.button('sin',3,1)
        self.button('cos',4,0)
        self.button('tan',4,1)
        self.button_show('credit',1,4)
        self.button_help('help',1,5)

    def entry(self, x_, y_):
        self.entry = Text(
            self.container, font=self.entry_font, state=DISABLED,
            height=self.button_height//2, width=self.button_width*5)
        self.entry.grid(row=x_, column=y_, columnspan=6, sticky='we')

    def button(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=lambda: self.normal_button_click(char_))
        self.b.grid(row=x_, column=y_)

    def button_eq(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.equal_button_click)
        self.b.grid(row=x_, column=y_, sticky='we', columnspan=2)

    def button_rem(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.rem_button_click)
        self.b.grid(row=x_, column=y_)

    def button_clear(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.clear_button_click)
        self.b.grid(row=x_, column=y_)

    def button_show(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=lambda: self.normal_button_click("Mia,Leila,Deangelo"))
        self.b.grid(row=x_, column=y_)

    def button_help(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=lambda: self.normal_button_click("For simple math:D"))
        self.b.grid(row=x_, column=y_)

    def display(self, text_):
        self.entry.config(state=NORMAL)
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', text_)
        self.entry.config(state=DISABLED)

    def normal_button_click(self, text_):
        self.string = '' + self.string + text_
        self.display(self.string)

    def equal_button_click(self):
        self.display(eval(self.string))
        self.string = ''

    def rem_button_click(self):
        self.string = '' + self.string[0:-1]
        self.display(self.string)

    def clear_button_click(self):
        self.display('')
        self.string = ''

    


class App:
    def __init__(self, master):
        self.master = master

        calc = Calculator(self.master, 0, 0)


root = Tk()
app = App(root)
root.title('The Interactive Calculator')
# root.play()
root.mainloop()
