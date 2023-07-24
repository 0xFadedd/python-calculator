# Python Calculator Project Documentation

## Overview

This project aims to create a simple calculator using Python's `tkinter` for the graphical user interface and a custom `PythonCalculator` class to handle the calculator's operations. The project is split into two main components:

1. `frontend.py` - This file is responsible for the graphical user interface of the calculator.
2. `python-calculator.py` - This file contains the `PythonCalculator` class, which handles the calculations.

---

## `frontend.py`

This file creates the user interface of the calculator using `tkinter`. It includes a class called `CalculatorGUI` that defines the calculator's layout and functionality.

### Functions to be completed

#### `button_click(self, value)`

This function is called when a button on the calculator is pressed. 

- **Inputs:** The function takes one input, `value`, which is the value of the button that was pressed.

- **Outputs:** This function does not return a value.

- **Functionality:** Currently, the function updates the entry field in the GUI and the `value` attribute in the `PythonCalculator` object to reflect the user's input. You should not need to modify this function.

#### `button_clear(self)`

This function is called when the 'Clear' button on the calculator is pressed.

- **Inputs:** This function does not take any inputs.

- **Outputs:** This function does not return a value.

- **Functionality:** You need to call the `clear` method from the `PythonCalculator` class here to reset the calculator's state.

#### `button_equal(self)`

This function is called when the '=' button on the calculator is pressed.

- **Inputs:** This function does not take any inputs.

- **Outputs:** This function does not return a value.

- **Functionality:** Here, you need to call the `calculate` method from your `PythonCalculator` class to compute the result of the user's input. 

---

## `python-calculator.py`

This file contains the `PythonCalculator` class which is responsible for performing the actual calculations in the calculator. 

### Functions to be completed

#### `clear(self)`

This function is called to clear the calculator's state.

- **Inputs:** This function does not take any inputs.

- **Outputs:** This function does not return a value.

- **Functionality:** You need to implement the clear functionality here. 

#### `add(self, value)`

This function is called to perform an addition operation.

- **Inputs:** The function takes one input, `value`, which is the value to be added.

- **Outputs:** This function does not return a value.

- **Functionality:** You need to implement the addition functionality here.

#### `subtract(self, value)`

This function is called to perform a subtraction operation.

- **Inputs:** The function takes one input, `value`, which is the value to be subtracted.

- **Outputs:** This function does not return a value.

- **Functionality:** You need to implement the subtraction functionality here.

#### `multiply(self, value)`

This function is called to perform a multiplication operation.

- **Inputs:** The function takes one input, `value`, which is the value to be multiplied.

- **Outputs:** This function does not return a value.

- **Functionality:** You need to implement the multiplication functionality here.

#### `divide(self, value)`

This function is called to perform a division operation.

- **Inputs:** The function takes one input, `value`, which is the value to be divided.

- **Outputs:** This function does not return a value.

- **Functionality:** You need to implement the division functionality here.

#### `calculate(self)`

This function is called to calculate the result of the user's input.

- **Inputs:** This function does not take any inputs.

- **Outputs:** This function should return the result of the calculation.

- **Functionality:** You need to implement the calculation logic here. This function should parse the `value` string, perform the appropriate operations (using the `add`, `subtract`, `multiply`, and `divide` methods), and return the result. You should handle both single and multiple operations, respecting the order of operations.