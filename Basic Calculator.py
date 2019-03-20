
from tkinter import *
class Calculator:
    def __init__(self, master):  # master == root or mainwindow
        self.master = master
        self.master.configure(background = "black")
        self.master.minsize(width = 300, height = 200)
        self.labelText = ""
        self.numHolder = None
        self.labelFrame = Frame(self.master)
        self.labelFrame.pack(side = TOP)
        self.buttonFrame = Frame(self.master)
        self.buttonFrame.pack(side = BOTTOM)
        self.screen = Label(self.labelFrame, text = self.labelText, bg = "black", fg = "red")
        self.screen.config(font = ("Times New Roman", 32))
        self.screen.pack(expand = 2, fill = BOTH)
        self.symbol = ""
        self.count = 0
        self.count1 = 0
        self.tempvar = ""
        self.make_symbols()
        self.make_numbers()
        
        
    def make_button(self, text, row, column, command = None):
        button = Button(self.buttonFrame, text = text, command = command)
        button.config(font = ("Times New Roman", 28))
        button.grid(row = row, column = column, sticky = W + E + N + S)
        return button
    
    
    def make_symbols(self):
        self.AC = self.make_button("AC", 1, 0, command = self.AC_function)
        self.plus_minus = self.make_button(" ± ", 1, 1, command = self.plus_minus_function)
        self.percent = self.make_button(" % ", 1, 2, command = self.percent_function)
        self.divide = self.make_button(" ÷ ", 1, 3, command = self.divide_function)
        self.multiply = self.make_button("×", 2, 3, command = self.multply_function)
        self.subtract = self.make_button("-", 3, 3, command = self.subtract_function)
        self.add = self.make_button("+", 4, 3, command = self.add_function)
        self.equals = self.make_button("=", 5, 3, command = self.equals_function)
        self.destroy = self.make_button("Exit",0,0,command = root.destroy)
        self.destroy.grid(columnspan = 2)
        #self.integral = self.make_button(u"\u222B",0,0,command = print(""))
        #self.derivative = self.make_button(u"\u2202",0,1,command = print(""))
        self.power = self.make_button("y^x",0,2,command = self.power_function)
        self.power.grid(columnspan = 2)


    def make_numbers(self):
        self.seven = self.make_button('7', 2, 0)
        self.eight = self.make_button('8', 2, 1)
        self.nine = self.make_button('9', 2, 2)
        self.four = self.make_button('4', 3, 0)
        self.five = self.make_button('5', 3, 1)
        self.six = self.make_button('6', 3, 2)
        self.one = self.make_button('1', 4, 0)
        self.two = self.make_button('2', 4, 1)
        self.three = self.make_button('3', 4, 2)
        self.zero = self.make_button('0', 5, 0)
        self.zero.grid(columnspan = 2)
        self.decimal = self.make_button('.', 5, 2)

        self.seven.bind('<Button-1>', lambda self2: self.button_command(7))
        self.eight.bind('<Button-1>', lambda self2: self.button_command(8))
        self.nine.bind('<Button-1>', lambda self2: self.button_command(9))
        self.four.bind('<Button-1>', lambda self2: self.button_command(4))
        self.five.bind('<Button-1>', lambda self2: self.button_command(5))
        self.six.bind('<Button-1>', lambda self2: self.button_command(6))
        self.one.bind('<Button-1>', lambda self2: self.button_command(1))
        self.two.bind('<Button-1>', lambda self2: self.button_command(2))
        self.three.bind('<Button-1>', lambda self2: self.button_command(3))
        self.zero.bind('<Button-1>', lambda self2: self.button_command(0))
        self.decimal.bind('<Button-1>', lambda self2: self.button_command("."))


    def button_command(self, num):
        if '.' in self.labelText and num == '.':
            pass
        else:
            self.labelText += str(num)
            self.screen.config(text=self.labelText)


    #button functions

    def AC_function(self):
        self.labelText = ""
        self.numHolder = None
        self.tempvar = ""
        self.count = 0
        self.count1 = 0
        self.screen.config(text = self.labelText)

    def plus_minus_function(self):
        try:
            value = float(self.labelText)
            value = -value
            self.labelText = str(value)
            self.screen.configure(text = self.labelText)
        except:
            pass

    def percent_function(self):
        try:
            self.labelText = str(float(self.labelText) / 100)
            self.screen.config(text=self.labelText)
        except:
            pass

    def divide_function(self):
        if self.labelText != "" and self.labelText != ".":
            self.numHolder = self.labelText
            self.labelText = ""
            self.screen.configure(text = self.labelText)
            self.symbol = "/"
            self.count += 1
            self.count1 = 0
    def multply_function(self):
        if self.labelText != "" and self.labelText != ".":
            self.numHolder = self.labelText
            self.labelText = ""
            self.screen.configure(text = self.labelText)
            self.symbol = "*"
            self.count += 1
    def subtract_function(self):
        if self.labelText != "" and self.labelText != ".":
            self.numHolder = self.labelText
            self.labelText = ""
            self.screen.configure(text = self.labelText)
            self.symbol = "-"
            self.count += 1
    def add_function(self):
        if self.labelText != "" and self.labelText != ".":
            self.numHolder = self.labelText
            self.labelText = ""
            self.screen.configure(text = self.labelText)
            self.symbol = "+"
            self.count += 1
    def power_function(self):
        if self.labelText != "" and self.labelText != ".":
            self.numHolder = self.labelText
            self.labelText = ""
            self.screen.configure(text = self.labelText)
            self.symbol = "**"
            self.count += 1
            self.count1 == 0
    def equals_function(self):
        if self.count == 2:
            y = self.labelText
            x = self.numHolder
            self.numHolder = self.labelText
            self.labelText = ""
            self.count = 1
        else:
            x = self.labelText
            if (self.symbol == "/" or self.symbol == "**") and self.count1 == 0:
                self.tempvar = self.labelText
                self.count1 = 1
                self.labelText = ""
                y = self.numHolder
            elif (self.symbol == "/" or self.symbol == "**") and self.count1 == 1:
                y = self.labelText
                x = self.tempvar
            else:
                self.labelText = ""
                y = self.numHolder
        self.labelText = str(eval(y+self.symbol+x))
        self.screen.configure(text = self.labelText)
root = Tk()
root.title('Basic Calculator')
App = Calculator(root)
root.mainloop()
