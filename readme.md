# Calculator in python

---

### Project Setup: 

1. Open Terminal by goint Terminal > New Terminal

2. Paste `python3 -m venv pythonVENV` in the terminal and hit enter

3. Then paste `.\pythonVENV\Scripts\activate` and hit enter to start the virtual environment

(mac): `source pythonVENV/bin/activate`

4. Then paste `cd src` and hit enter to get into the code file

5. Now you can start working on and running your code!



### Running Files

- Run tests by running 

```bash
python3 tests.py
```

- Run actual file by runnning

```bash
python3 frontend.py
```


---

### Guide

#### Part 1: `python_calculator.py`

As per the documentation in [on github (click here)](https://github.com/0xFadedd/python-calculator/tree/main/src), the python_calculator is an object that has a `calculation` attribute which represents the string of text present on the screen of the calculator. It also has a `memory` attribute which holds the most recent calculated value (defaults to 0). For example, memory will start by being 0. If you have the calculation `2+2+2` it should become `memory = 2`, then add 2 so `memory = 4`, then add 2 so `memory = 6`.  

1. Start by implementing the `clear` method functionality. All this function needs to do is clear the memory of the calculator object (it already clears the calculator screen).
2. Then implement the functionality for the operation methods (add, subtract, divide, multiply). All these functions take a `value` as an input. These functions need to modify the memory using the operation the function represents (e.g. add, subtract etc) and the value of the input.

    **EXAMPLE:**
    - if `memory = 4` and you run `add(4)`, you should end up with `memory = 8`

3. You then need to implement the calculate method; this is the trickiest bit!
To do this, you need to write code, that reads through each character of the `calculation` string and looks for operations, and then runs the calculation using the numbers either side. 
**REMEMBER:** You still need to follow the order of operations `(/,*,+,-)` e.g. check for divide, calculate, then check for multiply, calculate, etc etc. 
**NOTE:** You don't need to implement functionality for exponents or brackets


#### Part 2: `frontend.py`

This bit is about linking the user interface of the calculator to the `python_calculator.py` you have written. You will only need to implement the `button_click`, `button_clear`, and `button_equal` methods. Also note that `self.calculator` on line 12 of the file is a reference to the code in your `python_calculator.py` file. 

You can access the methods in your `python_calculator.py` file by using:
```python
self.calculator.methodName()
```
where `methodName` is just the name of the method you want to use e.g. `add` or `subtract` etc.

1. For the `button_click` method, you just need to update the `calculation` value of the `python_calculator` object.
2. For the `button_clear` method, you just need to call the `clear` method of the calculator object.
3. For the `button_equal` method, you need to call the `calculate` method of the calculator object.