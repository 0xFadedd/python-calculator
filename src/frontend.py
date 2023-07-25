#!/usr/bin/env python

import tkinter as tk
import python_calculator as pc

class CalculatorGUI:
    def __init__(self, root):
        self.application = root
        self.application.title('Python Calculator')

        # Instantiate the PythonCalculator
        self.calculator = pc.PythonCalculator()

        # Entry field
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons (0-9, +, -, *, /, C, =)
        # Number buttons
        for i in range(9):
            button = tk.Button(root, text=str(i+1), padx=40, pady=20, command=lambda i=i: self.button_click(i+1))
            button.grid(row=1+(i // 3), column=(i % 3))

        # Zero button
        button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        button_0.grid(row=4, column=0)

        # Clear button
        button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=self.button_clear)
        button_clear.grid(row=4, column=1, columnspan=2)

        # Arithmetic buttons
        button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: self.button_click("+"))
        button_add.grid(row=5, column=0)

        button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=lambda: self.button_click("-"))
        button_subtract.grid(row=6, column=0)

        button_multiply = tk.Button(root, text="*", padx=42, pady=20, command=lambda: self.button_click("*"))
        button_multiply.grid(row=5, column=1)

        button_divide = tk.Button(root, text="/", padx=42, pady=20, command=lambda: self.button_click("/"))
        button_divide.grid(row=6, column=1)

        button_equal = tk.Button(root, text="=", padx=91, pady=20, command=self.button_equal)
        button_equal.grid(row=5, column=2, rowspan=2)

    def button_click(self, value):
        # Append the clicked value to the user's input
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current + str(value))
        # Update the stored value in the calculator
        # Use to get the current string being shown self.entry.get()

    def button_clear(self):
        # Implement click event for clear button
        # Here you can call the clear method from your calculator class

        self.entry.delete(0, tk.END)

    def button_equal(self):
        # Implement click event for equal button
       
        result = 0 # Here you can call the calculate method from your calculator class and replace 0
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, str(result))

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
