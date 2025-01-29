import unittest
from string_calculator import add  # Import the function from your main file

class TestStringCalculator(unittest.TestCase):
	def test_multiple_numbers(self):
		self.assertEqual(add("1,2,3,4,5"), 15)

if __name__ == "__main__":
	unittest.main()