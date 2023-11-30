import unittest
from calc import add, subtract, multiply, divide, perform_operation


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5, 3), 8)  # Test addition with positive numbers
        self.assertEqual(add(-2, 7), 5)  # Test addition with one negative number

    def test_subtraction(self):
        self.assertEqual(subtract(10, 4), 6)  # Test subtraction with positive numbers
        self.assertEqual(subtract(5, -3), 8)  # Test subtraction with one negative number

    def test_multiplication(self):
        self.assertEqual(multiply(3, 4), 12)  # Test multiplication with positive numbers
        self.assertEqual(multiply(-2, -5), 10)  # Test multiplication with two negative numbers

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)  # Test division with positive numbers
        self.assertEqual(divide(-15, 3), -5)  # Test division with one negative number
        self.assertEqual(divide(5, 0), "Cannot divide by zero.")  # Test division by zero

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):  # Test if ValueError is raised for an invalid operation
            perform_operation(5, 2, '^')

    def test_float_result(self):
        result = divide(7, 3)
        self.assertAlmostEqual(result, 2.333, places=3)  # Test division with a floating-point result

    def test_addition_string(self):
        result = add('Hello', 'World')
        self.assertEqual(result, 'HelloWorld')  # Test addition with strings

    def test_subtraction_string(self):
        with self.assertRaises(TypeError):  # Test if TypeError is raised when subtracting strings
            subtract('abc', 'def')

    def test_multiply_by_zero(self):
        result = multiply(10, 0)
        self.assertEqual(result, 0)  # Test multiplication by zero

    def test_divide_by_negative(self):
        result = divide(20, -5)
        self.assertEqual(result, -4)  # Test division by a negative number


if __name__ == '__main__':
    unittest.main()
