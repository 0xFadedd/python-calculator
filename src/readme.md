# Python Calculator Project Documentation

## Overview

This project aims to create a simple calculator using Python's `tkinter` for the graphical user interface and a custom `PythonCalculator` class to handle the calculator's operations. The project is split into two main components:

1. `frontend.py` - This file is responsible for the graphical user interface of the calculator.
2. `python-calculator.py` - This file contains the `PythonCalculator` class, which handles the calculations.

---

## `frontend.py`

This file creates the user interface of the calculator using `tkinter`. It includes a class called `CalculatorGUI` that defines the calculator's layout and functionality.

### Functions to be completed

---

#### `button_click(self, value)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| `value` (value of the button pressed) | No return value | This function is called when a button on the calculator is pressed. It updates the entry field in the GUI and the `value` attribute in the `PythonCalculator` object to reflect the user's input. |

---

#### `button_clear(self)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| No inputs | No return value | This function is called when the 'Clear' button on the calculator is pressed. You need to call the `clear` method from the `PythonCalculator` class here to reset the calculator's state. |

---

#### `button_equal(self)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| No inputs | No return value | This function is called when the '=' button on the calculator is pressed. Here, you need to call the `calculate` method from your `PythonCalculator` class to compute the result of the user's input. |

---

## `python-calculator.py`

This file contains the `PythonCalculator` class which is responsible for performing the actual calculations in the calculator. 

### Functions to be completed

---

#### `clear(self)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| No inputs | No return value | This function is called to clear the calculator's state. You need to implement the clear functionality here. |

---

#### `add(self, value)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| `value` (value to be added) | No return value | This function is called to perform an addition operation. You need to implement the addition functionality here. |

---

#### `subtract(self, value)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| `value` (value to be subtracted) | No return value | This function is called to perform a subtraction operation. You need to implement the subtraction functionality here. |

---

#### `multiply(self, value)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| `value` (value to be multiplied) | No return value | This function is called to perform a multiplication operation. You need to implement the multiplication functionality here. |

---

#### `divide(self, value)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| `value` (value to be divided) | No return value | This function is called to perform a division operation. You need to implement the division functionality here. |

---

#### `calculate(self)`

| Inputs | Outputs | Functionality |
| :----- | :------ | :------------ |
| No inputs | Returns the result of the calculation | This function is called to calculate the result of the user's input. You need to implement the calculation logic here. This function should parse the `value` string, perform the appropriate operations (using the `add`, `subtract`, `multiply`, and `divide` methods), and return the result. You should handle both single and multiple operations, respecting the order of operations. |

---