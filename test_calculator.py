import unittest

from calculator import add, multiply, subtract  # Import the functions to be tested


class TestCalculator(unittest.TestCase):
    """
    Unit tests for our calculator functions.
    """

    def test_add(self):
        """
        Test the add function with positive, negative, and zero values.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        """
        Test the multiply function.
        """
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(0, 100), 0)

    def test_subtract(self):
        """
        Test the subtract function.
        """
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)


# This allows the test file to be run directly from the command line
if __name__ == "__main__":
    unittest.main()
