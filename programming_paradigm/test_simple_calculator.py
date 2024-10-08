import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Create an instance of SimpleCalculator for testing."""
        self.calculator = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 5), -5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calculator.multiply(3, 7), 21)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(0, 10), 0)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(5, 0), None)  # Test division by zero
        self.assertEqual(self.calculator.divide(-10, 2), -5)

if __name__ == '__main__':
    unittest.main()


