import unittest
from string_calculator import add  # Import the function from your main file

class TestStringCalculator(unittest.TestCase):
	def test_single_number(self):
		self.assertEqual(add("1"), 1)

if __name__ == "__main__":
	unittest.main()