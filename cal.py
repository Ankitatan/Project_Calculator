from tkinter import Tk, Entry, Button, StringVar, Frame

import math

class Calculator:
    def __init__(self, master):
        master.title("Interactive Calculator")
        master.geometry('400x500')
        master.config(bg='lightblue')

        self.equation = StringVar()
        self.entry_value = ''

        # Configure rows and columns for dynamic resizing
        master.rowconfigure(0, weight=1)
        for i in range(1, 6):
            master.rowconfigure(i, weight=1)
        for i in range(4):
            master.columnconfigure(i, weight=1)

        # Input field
        self.create_display(master)

        # Buttons
        self.create_buttons(master)

        # Keyboard bindings
        master.bind('<Key>', self.handle_keypress)

    def create_display(self, master):
        # Entry field for input
        entry = Entry(master, bg='light cyan', font=('Arial Bold', 24), textvariable=self.equation, justify='center', bd=15)
        entry.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=5, pady=5)

    def create_buttons(self, master):
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), 
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), 
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), 
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), 
            ('%', 5, 0), ('log', 5, 1), ('.', 5, 2),
            ('(', 6, 0), (')', 6, 1), ('/', 6, 2),
            ('*', 7, 0),('-', 7, 1),('+', 7, 2)
        ]

        # Create buttons with hover effect
        for (text, row, col) in buttons:
            if text == '=':
                Button(master, text=text, bg='#4CAF50', fg='white', font=('Arial', 18, 'bold'),
                       command=self.solve).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            elif text == 'C':
                Button(master, text=text, bg='#f44336', fg='white', font=('Arial', 18, 'bold'),
                       command=self.clear).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            elif text == '%':
                Button(master, text=text, bg='#f0f0f0', fg='black', font=('Arial', 18, 'bold'),
                       command=self.calculate_percentage).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            elif text == 'log':
                Button(master, text=text, bg='#f0f0f0', fg='black', font=('Arial', 18, 'bold'),
                       command=self.calculate_logarithm).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            else:
                Button(master, text=text, bg='#f0f0f0', fg='black', font=('Arial', 18, 'bold'),
                       command=lambda value=text: self.show(value)).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)  # Update entry_value
        except:
            self.equation.set("Error")
            self.entry_value = ''

    def calculate_percentage(self):
        try:
            result = eval(self.entry_value) / 100
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

    def calculate_logarithm(self):
        try:
            result = math.log10(float(self.entry_value))
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

    def handle_keypress(self, event):
        # Handle numeric, operator, and control keys
        key = event.char
        if key in '0123456789+-*/.%()':
            self.show(key)
        elif key == '\r':  # Enter key
            self.solve()
        elif key == '\x08':  # Backspace key
            self.entry_value = self.entry_value[:-1]
            self.equation.set(self.entry_value)


# Create and run the calculator
root = Tk()
calculator = Calculator(root)
root.mainloop()