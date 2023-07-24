import unittest
import python_calculator as pc

# DO NOT TOUCH THIS CODE
class TestPythonCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = pc.PythonCalculator()

    def test_clear(self):
        self.calculator.memory = 1
        self.calculator.value = 1

        self.calculator.clear()
        self.assertEqual(self.calculator.value, '')
        self.assertEqual(self.calculator.memory, 0)

    def test_add(self):
        self.calculator.add(5)
        self.assertEqual(self.calculator.memory, 5)

        self.calculator.memory = -3
        self.calculator.add(5)
        self.assertEqual(self.calculator.memory, 2)

        self.calculator.memory = 2
        self.calculator.add(-5)
        self.assertEqual(self.calculator.memory, -3)


    def test_subtract(self):
        self.calculator.subtract(3)
        self.assertEqual(self.calculator.memory, -3)

        self.calculator.memory = 0
        self.calculator.subtract(-3)
        self.assertEqual(self.calculator.memory, 3)

    def test_multiply(self):
        self.calculator.memory = 10
        self.calculator.multiply(3)
        self.assertEqual(self.calculator.memory, 30)

        self.calculator.memory = 10
        self.calculator.multiply(-3)
        self.assertEqual(self.calculator.memory, -30)

    def test_divide(self):
        self.calculator.memory = 10
        self.calculator.divide(2)
        self.assertEqual(self.calculator.memory, 5)

        self.calculator.memory = 10
        self.calculator.divide(-2)
        self.assertEqual(self.calculator.memory, -5)

    def test_calculate(self):
        self.calculator.value = '2+2*2'
        self.assertEqual(self.calculator.calculate(), 6)

if __name__ == '__main__':
    unittest.main()
